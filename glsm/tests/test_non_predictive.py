from glsm.non_predictive.model import NonPredictive
from glsm.non_predictive.features import Feature

def test_non_predictive_instance(non_predictive_model):
    assert isinstance(non_predictive_model, NonPredictive)
    assert non_predictive_model.features[0].name == "Monthly Users"

def test_sum_squares_normalized_weights_is_one(non_predictive_model):
    features = non_predictive_model.features
    weights_sqr_sum = sum(
        [feature.normalized_weight**2 for feature in features]
    )
    assert weights_sqr_sum == 1

def test_compute_lambda_equals_75 (non_predictive_model, lead):
    model = non_predictive_model
    lambda_value = model.compute_lambda(lead)

    assert lambda_value == 75.4

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

def test_qualification_assessement_true(non_predictive_model, lead):
    model = non_predictive_model
    assert model.assess_qualification(lead) == True

def test_qualification_assessement_false(non_predictive_model, lead):
    model = non_predictive_model
    model.qualification_threshold = 90
    assert model.assess_qualification(lead) == False

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

# def test_should_return_points_assiment_suggestion(non_predictive_model,):
#     model = non_predictive_model
#     suggeston = model.suggest_points_assignment()
#     assert suggeston == {
#         "Monthly Users": {
#             "Up to 50K": 50,
#             "50K - 100K": 60,
#             "100K - 200K": 80,
#             "More than 200K": 100
#         },
#         "Industry": {
            # "Agriculture": 10,
            # "Transportation": 90,
            # "Healthcare": 40,
            # "Manufacturing": 50,
            # "Education": 20,
            # "Finance": 30,
            # "Technology": 70,
            # "Retail": 60,
            # "Telecom": 80,
            # "Other": 100
#         }


# Agriculture
# Transportation
# Healthcare
# Manufacturing
# Education
# Finance
# Technology
# Retail
# Telecom
# Other