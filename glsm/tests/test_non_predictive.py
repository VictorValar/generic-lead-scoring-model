import pandas as pd

from glsm.non_predictive.model import NonPredictive
from glsm.non_predictive.features import Feature


def test_non_predictive_instance(non_predictive_model):
    assert isinstance(non_predictive_model, NonPredictive)
    assert non_predictive_model.features[0].name == "Monthly Users"


def test_sum_squares_normalized_weights_is_one(non_predictive_model):
    features = non_predictive_model.features
    weights_sqr_sum = sum(feature.normalized_weight ** 2 for feature in features)
    assert weights_sqr_sum == 1


def test_compute_lambda_equals_75(non_predictive_model, lead):
    model = non_predictive_model
    lambda_value = model.compute_lambda(lead)

    assert lambda_value == 75.4


def test_add_features(non_predictive_model):
    model = non_predictive_model

    feature_d = Feature(
        name="test d",
        weight=0.5,
        points_map=[
            ("Up to 50K", 10),
            ("50K - 100K", 30),
            ("100K - 200K", 50),
            ("More than 200K", 100),
        ],
        options_df=pd.DataFrame([
            {"label": "Up to 50K", "is_ICP": False, "points": 0},
            {"label": "50K - 100K", "is_ICP": True, "points": 0},
            {"label": "100K - 200K", "is_ICP": False, "points": 0},
            {"label": "More than 200K", "is_ICP": False, "points": 0},
        ])
    )

    feature_e = Feature(
        name="test e",
        weight=0.5,
        points_map=[
            ("Up to 50K", 10),
            ("50K - 100K", 30),
            ("100K - 200K", 50),
            ("More than 200K", 100),
        ],
        options_df=pd.DataFrame([
            {"label": "AAA", "is_ICP": False, "points": 20},
            {"label": "BBB", "is_ICP": True, "points": 10},
            {"label": "CCC", "is_ICP": False, "points": 30},
            {"label": "DDD", "is_ICP": False, "points": 40},
        ])
    )

    model.add_features([feature_d, feature_e])

    assert len(model.features) == 5


def test_describe_features(non_predictive_model):
    model = non_predictive_model

    description = model.describe_features()

    assert description == {
        "Monthly Users": {
            "weight": 0.5, "normalized_weight": 0.44
        },
        "Industry": {
            "weight": 0.25, "normalized_weight": 0.22
        },
        "Mkt Investment": {
            "weight": 1, "normalized_weight": 0.87
        }
    }


def test_should_remove_features(non_predictive_model):
    model = non_predictive_model

    model.remove_features(["Monthly Users", "Industry"])

    assert model.features[0].name == "Mkt Investment"
    assert len(model.features) == 1


def test_qualification_assessment_true(non_predictive_model, lead):
    model = non_predictive_model
    assert model.assess_qualification(lead) is True


def test_qualification_assessment_false(non_predictive_model, lead):
    model = non_predictive_model
    model.qualification_threshold = 90
    assert model.assess_qualification(lead) is False


def test_compute_qualification_threshold_should_return_50(non_predictive_model):
    model = non_predictive_model
    model.compute_qualification_threshold()
    assert model.qualification_threshold == 50


def test_compute_normalized_weights(non_predictive_model):
    model = non_predictive_model
    model.compute_normalized_weights()
    assert round(
        model.features[0].normalized_weight,
        model.round_decimals
    ) == 0.44


def test_auto_assign_points(non_predictive_model):
    model = non_predictive_model
    model.auto_assign_points()
    assert model.features[1].options_df.loc[0, "label"] == "Other"
    assert model.features[1].options_df.loc[0, "is_ICP"] is False
    assert model.features[1].options_df.loc[0, "points"] == 0

    assert model.features[1].options_df.loc[3, "label"] == "Healthcare"
    assert model.features[1].options_df.loc[3, "is_ICP"] is False
    assert model.features[1].options_df.loc[3, "points"] == 30

    assert model.features[1].options_df.loc[9, "label"] == "Telecom"
    assert model.features[1].options_df.loc[9, "is_ICP"] is False
    assert model.features[1].options_df.loc[9, "points"] == 100

    assert model.features[0].points_map == [
        ["Up to 50K", 0],
        ["50K - 100K", 50],
        ["100K - 200K", 75],
        ["More than 200K", 100],
    ]


def test_preview_auto_assign_points(non_predictive_model):
    model = non_predictive_model
    preview = model.auto_assign_points(preview=True)
    assert model.features[1].options_df.loc[3, "points"] == 0
    assert model.features[1].options_df.loc[9, "points"] == 0
    assert preview.loc[1, 'points'] == 50
    assert preview.loc[19, 'points'] == 100
