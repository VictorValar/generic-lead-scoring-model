from pydantic import BaseModel, conlist
from typing import List, Optional

from glsm.features import Feature

class NonPredictive(BaseModel):
    features: conlist(Feature) = []

    def add_feature(self, feature: Feature):

        if isinstance(feature, Feature):
            self.features.append(feature)
        else:
            raise TypeError("Feature must be of type Features")

