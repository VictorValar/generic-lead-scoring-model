from pydantic import BaseModel, conlist
from typing import List
from glsm.features import Feature
import math

class NonPredictive(BaseModel):
    '''
    A non predictive lead scoring model.

    Returns True if param1 is equal to param2's length.

    Args:
        features: List of features of the model
        round_decimals: Number of decimals to round the lambda value, default is 2

    Returns:
        float: The computed lambda value, rounded to the number of decimals specified in the model

    '''
    features: conlist(Feature) = []
    round_decimals: int = 2

    def add_features(self, features: List[Feature]):
        '''
        Adds a list of features to the model.

        Must be of type Feature otherwise raises a TypeError.

        Args:
            features (List[Feature]): List of features to be added to the model

        Raises:
            TypeError: If features is not of type List[Feature]

        '''
        for feature in features:
            if not isinstance(feature, Feature):
                raise TypeError("All element of the list must be of type Feature")

        self.features.extend(features)

    def compute_lambda(self, lead: dict) -> float:
        '''
        Computes Lead score of a given lead.

        Lead score is the dot product of the normalized weights and the points assigned to the labels of the features.

        Args:
            lead (dict): A dictionary containing feature names as keys and feature label as values.
            Example: lead = {"feature_name": "label"},...}

        Returns:
            float: The computed lambda value, rounded to the number of decimals specified in the model
        '''

        self.compute_normalized_weights()

        lambda_value = sum(
            [
                (feature.normalized_weight**2) * feature.get_points(lead[feature.name])
                for feature in self.features
            ]
        )

        return round(lambda_value, self.round_decimals)

    def compute_normalized_weights(self):
        '''
        Computes the normalized weights of the model features.

        The normalized weight of a feature is the weight of the feature divided by the magnitude of the weights of all the features.
        '''

        magnitude = math.sqrt(
            sum([feature.weight**2 for feature in self.features])
        )

        for feature in self.features:
            feature.normalized_weight = feature.weight / magnitude



