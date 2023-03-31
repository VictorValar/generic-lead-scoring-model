from pydantic import BaseModel, validator
from typing import List, Tuple, Optional



class Feature(BaseModel):
    '''
    A feature of a model.
    @param name: Name of the feature
    @param points_map: A list of tuples containing the label and the points assigned to the label (label, points). Example: [('label1', 1), ('label2', 2)]
    @param weight: Weight of the feature
    '''

    name: str
    points_map: List[Tuple[str, float]] # (label, points)
    weight: float
    normalized_weight: float = None

    def get_points(self, label: str) -> float:
        '''
        Returns the points assigned to the label of a feature.
        '''
        for item in self.points_map:
            if item[0] == label:
                return item[1]
        return None







