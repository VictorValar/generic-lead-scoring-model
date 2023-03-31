from pydantic import BaseModel, conlist
from typing import List, Optional
from glsm.features import Feature
import math

class NonPredictive(BaseModel):
    features: conlist(Feature) = []

    def add_feature(self, feature: Feature):
        '''
        Adds a feature to the model.
        Must be of type Feature otherwise raises a TypeError
        '''

        if isinstance(feature, Feature):
            self.features.append(feature)
        else:
            raise TypeError("Features must be of type Feature")


    def compute_normalized_weights(self):
        '''
        Computes the normalized weights of the features
        '''

        magnitude = math.sqrt(
            sum([feature.weight**2 for feature in self.features])
        )

        for feature in self.features:
            feature.normalized_weight = feature.weight / magnitude



