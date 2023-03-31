from typing import List
from glsm.non_predictive import NonPredictive
from glsm.features import Feature
import logging

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
    weights_sqr_sum = sum([feature.normalized_weight**2 for feature in features])
    assert weights_sqr_sum == 1