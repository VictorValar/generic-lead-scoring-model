from pydantic import BaseModel, Field, validator
from typing import List, Optional, Union

from glsm.features import Features

class NonPredictive(BaseModel):
    def __init__(self, ):
        id: int
        features = List[Features]
