from typing import List
from glsm.non_predictive import NonPredictive
from glsm.features import Feature

def test_is_instance_non_predictive(non_predictive_model):
    assert isinstance(non_predictive_model, NonPredictive)

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

def test_compute_lambda_equals_50 (non_predictive_model, lead):

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


