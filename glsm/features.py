from pydantic import BaseModel, validator
from typing import List, Tuple, Optional



class Feature(BaseModel):
    '''
    A feature of a model
    '''
    name: str
    points_map: List[Tuple[str, float]]
    weight: float
    normalized_weight: float = None

    # class Config:
    #     arbitrary_types_allowed = True







