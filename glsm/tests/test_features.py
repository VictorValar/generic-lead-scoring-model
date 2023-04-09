from glsm.non_predictive.features import Feature
import pandas as pd


def test_feature_instance(feature_instances):
    assert isinstance(feature_instances[0], Feature)
    assert feature_instances[0].name == "Monthly Users"
    assert feature_instances[0].weight == 0.5
    assert feature_instances[0].points_map == [
        ["Up to 50K", 0],
        ["50K - 100K", 50],
        ["100K - 200K", 75],
        ["More than 200K", 100],
    ]
    assert feature_instances[1].name == "Industry"
    assert feature_instances[1].weight == 0.25
    assert feature_instances[1].points_map == [
        ["Other", 0],
        ["Agriculture", 0],
        ["Transportation", 0]
    ]


def test_features_first_element_types(feature_instances):
    p_map = feature_instances[0].points_map

    assert type(p_map[0][0]) == str
    assert type(p_map[0][1]) == float


def test_get_points(feature_instances):
    assert feature_instances[0].get_points("Up to 50K") == 0


def test_options_df_values(feature_instances):
    expected_df = pd.DataFrame([
        {"label": "Up to 50K", "is_ICP": False, "points": 0},
        {"label": "50K - 100K", "is_ICP": True, "points": 0},
        {"label": "100K - 200K", "is_ICP": False, "points": 0},
        {"label": "More than 200K", "is_ICP": False, "points": 0},
    ])
    assert feature_instances[0].options_df.equals(expected_df)

