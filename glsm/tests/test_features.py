from glsm.non_predictive.features import Feature

def test_feature_instance(feature_instance):
    assert isinstance(feature_instance , Feature)

def test_features_first_element_types(feature_instance):
    map = feature_instance.points_map

    assert type(map[0][0]) == str
    assert type(map[0][1]) == float

def test_compute_normalized_weights(non_predictive_model):
    model = non_predictive_model
    model.compute_normalized_weights()
    assert round(
        model.features[0].normalized_weight,
        model.round_decimals
    ) == 0.44

def test_get_points(feature_instance):
    assert feature_instance.get_points("Up to 50K") == 0

