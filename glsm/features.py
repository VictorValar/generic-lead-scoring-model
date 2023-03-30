from pydantic import BaseModel
from typing import List

class Options(BaseModel):
    points: int
    weights: float



class Features(BaseModel):
    options = List[Options]

    def normalize_weights(self):
        pass 
