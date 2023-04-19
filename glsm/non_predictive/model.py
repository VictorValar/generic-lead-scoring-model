import math
from typing import List, Tuple
import pandas as pd
from pydantic import BaseModel, conlist
from glsm.non_predictive.features import Feature



class NonPredictive(BaseModel):
    """
    A non-predictive lead scoring model.
    """
    features: conlist(Feature) = []
    round_decimals: int = 2
    qualification_threshold: float = 50
    points_range: Tuple[float, float] = (0, 100)

    def add_features(self, features: List[Feature]):
        """
        Adds a list of features_names to the model.

        All items must be of type Feature otherwise raises a TypeError.
        """
        for feature in features:
            if not isinstance(feature, Feature):
                raise TypeError("All element of the list must be of type Feature")

        self.features.extend(features)

    def remove_features(self, features_names: List[str]):
        """
        Removes a list of features_names from the model given their names.
        """

        for name in features_names:
            for feature in self.features:
                if feature.name == name:
                    self.features.remove(feature)

    def compute_lambda(self, lead: dict) -> float:
        """
        Computes Lead score of a given lead.
        """

        self.compute_normalized_weights()

        lambda_value = sum(
            (feature.normalized_weight ** 2) * feature.get_points(lead[feature.name])
            for feature in self.features
        )

        return round(lambda_value, self.round_decimals)

    def compute_normalized_weights(self):
        """
        Computes the normalized weights of the model features_names.

        The normalized weight of a feature is the weight of the feature divided by the magnitude of the weights of all
        the features_names.
        """

        magnitude = math.sqrt(sum(feature.weight ** 2 for feature in self.features))

        for feature in self.features:
            feature.normalized_weight = feature.weight / magnitude

    def compute_qualification_threshold(self, ):
        """
        Computes and returns the qualification threshold based on the points range set for the model.
        """

        points_min = self.points_range[0]
        points_max = self.points_range[1]

        try:
            theta = points_max - (points_max - points_min) / 2
        except TypeError as exc:
            raise TypeError("Points range must be a tuple of two numeric types") from exc

        self.qualification_threshold = theta

        return theta

    def describe_features(self, ):
        """
        Returns a dictionary with the features_names of the model and their weights.
        """

        self.compute_normalized_weights()

        description = {}

        for feature in self.features:
            description[feature.name] = {
                "weight": feature.weight,
                "normalized_weight": round(
                    feature.normalized_weight,
                    self.round_decimals
                )
            }
            print(description)

        return description

    def assess_qualification(self, lead):
        """
        Returns True if the lead equals of passes the qualification threshold for the model, False otherwise.
        """
        return self.compute_lambda(lead) >= self.qualification_threshold

    def auto_assign_points(self, preview: bool = False) -> pd.Dataframe:
        """
        Automatically assigns points to the of the model.
        :returns Dataframe
        """

        less_than_icp_remaining_points = self.qualification_threshold - self.points_range[0]
        more_than_icp_remaining_points = self.points_range[1] - self.qualification_threshold
        merged_df = pd.DataFrame()

        for feature in self.features:
            icp_index_range: List[int] = []
            df = feature.options_df.copy() if preview else feature.options_df

            for index, row in df.iterrows():
                if row['is_ICP'] is True:
                    df.loc[index, 'points'] = 50
                    icp_index_range.append(index)

            less_than_icp_options_index: List[int] = []
            more_than_icp_options_index: List[int] = []
            less_than_icp_options_count: int = 0
            more_than_icp_options_count: int = 0

            for index, row in df.iterrows():
                if row['is_ICP'] is False and index < icp_index_range[0]:
                    less_than_icp_options_index.append(index)
                    less_than_icp_options_count += 1
                if row['is_ICP'] is False and index > icp_index_range[-1]:
                    more_than_icp_options_index.append(index)
                    more_than_icp_options_count += 1

            step_down = - (less_than_icp_remaining_points / less_than_icp_options_count)
            step_up = more_than_icp_remaining_points / more_than_icp_options_count

            # Assign points to options less desirable than the ICP option
            for index in reversed(less_than_icp_options_index):

                new_points = df.loc[index + 1, 'points'] + step_down

                if new_points < 0:
                    df.loc[index, 'points'] = 0
                else:
                    df.loc[index, 'points'] = new_points

            # Assign points to options more desirable than the ICP option
            for index in more_than_icp_options_index:
                df.loc[index, 'points'] = df.loc[index - 1, 'points'] + step_up

            if not preview:
                feature.options_df = df

            merged_df = pd.concat([merged_df, df], ignore_index=True)

        return merged_df
