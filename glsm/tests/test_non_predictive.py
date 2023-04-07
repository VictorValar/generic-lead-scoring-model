from typing import List
from glsm.non_predictive import NonPredictive
from glsm.features import Feature

def test_is_instance_non_predictive(non_predictive_model):
    assert isinstance(non_predictive_model, NonPredictive)
    assert non_predictive_model.features[0].name == "Monthly Users"

def test_features_first_element_is_instance_Feature_class_istance(non_predictive_model):
    assert isinstance(non_predictive_model.features[0] , Feature)

def test_features_first_element_name_types(non_predictive_model):

    map = non_predictive_model.features[0].points_map

    assert type(map[0][0]) == str
    assert type(map[0][1]) == float


def test_sum_squares_normalized_weights(non_predictive_model):
    features = non_predictive_model.features
    weights_sqr_sum = sum(
        [feature.normalized_weight**2 for feature in features]
    )
    assert weights_sqr_sum == 1

def test_compute_lambda_equals_81 (non_predictive_model, lead):
    model = non_predictive_model
    lambda_value = model.compute_lambda(lead)

    assert lambda_value == 81.43

def test_add_featues(non_predictive_model ):
    model = non_predictive_model

    feature_d = Feature(
        name="test d",
        weight=0.5,
        points_map=[
            ("Up to 50K",50),
            ("50K - 100K",60),
            ("100K - 200K",80),
            ("More than 200K",100)
        ]
    )

    feature_e = Feature(
        name="test e",
        weight=0.5,
        points_map=[
            ("Up to 50K",10),
            ("50K - 100K",30),
            ("100K - 200K",50),
            ("More than 200K",100),
        ]

    )

    model.add_features([feature_d, feature_e])

    assert len(model.features) == 5


def test_should_remove_features(non_predictive_model):
    model = non_predictive_model

    model.remove_features(["Monthly Users", "Industry"])

    assert model.features[0].name == "Mkt Investment"
    assert len(model.features) == 1


def test_should_return_features_description(non_predictive_model):
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

def test_qualification_assessement_shlud_return_true(non_predictive_model, lead):
    model = non_predictive_model
    assert model.assess_qualification(lead) == True

def test_qualification_assessement_shlud_return_false(non_predictive_model, lead):
    model = non_predictive_model
    model.qualification_threshold = 90
    assert model.assess_qualification(lead) == False