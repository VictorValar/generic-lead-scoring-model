from pydantic import BaseModel
from typing import List, Tuple
from typing_extensions import TypedDict


class Feature(BaseModel):
    '''
    A feature of a model
    '''
    name: str
    points_map: List[Tuple[str, float]]

    class Config:
        arbitrary_types_allowed = True

    def normalize_weights(self):
        pass
