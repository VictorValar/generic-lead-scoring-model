from pydantic import BaseModel, conlist
from typing import List, Optional
from glsm.features import Feature
import math

class NonPredictive(BaseModel):
    '''
    A non predictive lead scoring model.
    @param features: List of features of the model
    @param round_decimals: Number of decimals to round the lambda value, default is 2
    '''
    features: conlist(Feature) = []
    round_decimals: int = 2

    def add_feature(self, feature: Feature):
        '''
        Adds a feature to the model.
        Must be of type Feature otherwise raises a TypeError
        '''

        if isinstance(feature, Feature):
            self.features.append(feature)
        else:
            raise TypeError("Features must be of type Feature")


    def compute_lambda(self, lead: dict) -> float:
        '''
        Computes the lambda value of the lead. Lead score(lambda) is the sum of the normalized weight of each feature multiplied by the points assined to each feature.
        @param lead: A dictionary containing feature names as keys and feature label as values
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
        Computes the normalized weights of the features
        '''

        magnitude = math.sqrt(
            sum([feature.weight**2 for feature in self.features])
        )

        for feature in self.features:
            feature.normalized_weight = feature.weight / magnitude



