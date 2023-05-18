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
    assert feature_instances[1].options_df.is_ICP.sum() == 1
    assert feature_instances[1].options_df.label[0] == "Other"
    assert feature_instances[1].options_df.label[1] == "Agriculture"
    assert feature_instances[1].options_df.label[2] == "Transportation"

