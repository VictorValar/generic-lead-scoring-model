from pydantic import BaseModel, validator, conlist
from typing import List, Union

class Feature(BaseModel):
    '''
    A feature of a model.

    Variables:
    points_map: A nested list containing the label of a feature and the points assigned to it: [[label, points],...]
    '''

    name: str
    points_map: conlist(
        List[Union[str, float]],
        min_items=1,
    )
    weight: float
    normalized_weight: float = None

    @validator('points_map', each_item=True)
    def validate_points_map(cls, points_map):

        try:
            label, points = points_map
        except ValueError as exc:
            # check err message to see if it's the right error keyword: unpack
            if 'not enough values to unpack (expected 2, got 1)' in str(exc):
                label = points_map[0]
                points = 0

        try:
            return [label, float(points)]
        except ValueError as exc:
            raise ValueError('Each item of Points map should be: [string, numeric value]') from exc

    def get_points(self, label: str) -> float:
        '''
        Returns the points assigned to the label of a feature.
        '''
        for item in self.points_map:
            if item[0] == label:
                return item[1]
        raise ValueError(f'Label {label} not found in points map')







