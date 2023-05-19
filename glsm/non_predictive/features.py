from pydantic import BaseModel, validator, conlist
from typing import List, Union
import pandas as pd


class _OptionsDataFrame(BaseModel):
    """
    This class is used to validate the options types of the DataFrame.
    Don't use it directly.
    """

    label: str
    is_ICP: bool = False
    points: Union[float, int, None] = None


class Feature(BaseModel):
    """
    A feature of a model that can be used to score a lead.
    """

    name: str
    options_df: pd.DataFrame
    weight: float
    normalized_weight: float = None

    class Config:
        arbitrary_types_allowed = True

    @validator('options_df', pre=True)
    def validate_options_df(cls, options_df: pd.DataFrame, values: dict) -> pd.DataFrame:
        options_dicts = options_df.to_dict(orient='records')

        # Validate each dictionary against _OptionsDataFrame schema
        [_OptionsDataFrame(**options_dict) for options_dict in options_dicts]

        feature_name = values.get('name')

        options_df['Feature Name'] = feature_name

        return options_df

    def get_points(self, label: str) -> float:
        """
        Returns the points assigned to the label of a feature.
        """
        for item in self.options_df.values:
            if item[0] == label:
                return item[2]
        raise ValueError(f'Label {label} not found in options Data Frame')
