import pytest

from glsm.non_predictive.features import Feature
import pandas as pd


def test_feature_instance(feature_instances):
    assert isinstance(feature_instances[0], Feature)
    assert feature_instances[0].name == "Monthly Users"
    assert feature_instances[0].weight == 0.5
    assert feature_instances[1].name == "Industry"
    assert feature_instances[1].weight == 0.25


def test_get_points(feature_instances):
    assert feature_instances[0].get_points("Up to 50K") == 0


def test_feature_instances_options_df_values(feature_instances):
    assert feature_instances[1].options_df.points.sum() == 0
    assert feature_instances[1].options_df.is_ICP.sum() == 3
    assert feature_instances[1].options_df.label[0] == "Other"
    assert feature_instances[1].options_df.label[1] == "Agriculture"
    assert feature_instances[1].options_df.label[2] == "Transportation"


def test_at_least_one_icp_in_options(feature_instances):
    """
    Checks if at least one is_ICP is set to True
    """
    with pytest.raises(ValueError, match="At least one option must be an ICP"):
        Feature(
            name="LLLL",
            weight=0.25,
            options_df=pd.DataFrame([
                {"label": "AAA", "is_ICP": False, "points": 0},
                {"label": "BBB", "is_ICP": False, "points": 0}
            ])
        )



def test_icp_options_are_grouped_together(feature_instances):
    """
    Checks if ICP options are grouped together
    """
    with pytest.raises(ValueError, match="ICP options must be grouped together"):
        feature = Feature(
            name="ZZZZ",
            weight=0.25,
            options_df=pd.DataFrame([
                {"label": "AAA", "is_ICP": False, "points": 0},
                {"label": "BBB", "is_ICP": True, "points": 0},
                {"label": "CCC", "is_ICP": False, "points": 0},
                {"label": "DDD", "is_ICP": True, "points": 0},
                {"label": "EEE", "is_ICP": True, "points": 0},
                {"label": "FFF", "is_ICP": True, "points": 0},
                {"label": "GGG", "is_ICP": False, "points": 0},
                {"label": "HHH", "is_ICP": True, "points": 0},
                {"label": "III", "is_ICP": False, "points": 0},
                {"label": "JJJ", "is_ICP": False, "points": 0},
            ])
        )
