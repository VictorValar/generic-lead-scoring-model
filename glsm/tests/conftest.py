from pytest import fixture
from glsm.non_predictive.model import NonPredictive
from glsm.non_predictive.features import Feature
import pandas as pd


@fixture
def non_predictive_model() -> NonPredictive:
    """
    Yields a NonPredictive() model with three features_names
    """
    model = NonPredictive()

    feature_a = Feature(
        name="Monthly Users",
        weight=0.5,
        options_df=pd.DataFrame([
            {"label": "Up to 50K", "is_ICP": False, "points": 0},
            {"label": "50K - 100K", "is_ICP": True, "points": 0},
            {"label": "100K - 200K", "is_ICP": False, "points": 0},
            {"label": "More than 200K", "is_ICP": False, "points": 0},
        ])
    )

    feature_b = Feature(
        name="Industry",
        weight=0.25,
        options_df=pd.DataFrame([
            {"label": "Other", "is_ICP": False, "points": 0},
            {"label": "Agriculture", "is_ICP": False, "points": 0},
            {"label": "Transportation", "is_ICP": False, "points": 0},
            {"label": "Healthcare", "is_ICP": False, "points": 0},
            {"label": "Manufacturing", "is_ICP": False, "points": 0},
            {"label": "Education", "is_ICP": True, "points": 0},
            {"label": "Finance", "is_ICP": True, "points": 0},
            {"label": "Technology", "is_ICP": True, "points": 0},
            {"label": "Retail", "is_ICP": False, "points": 0},
            {"label": "Telecom", "is_ICP": False, "points": 0},
        ])
    )

    feature_c = Feature(
        name="Mkt Investment",
        weight=1,
        options_df=pd.DataFrame([
            {"label": "Up to $50K", "is_ICP": False, "points": 0},
            {"label": "50k - $100K", "is_ICP": True, "points": 0},
            {"label": "100k - $200K", "is_ICP": False, "points": 0},
            {"label": "$200K - $300K", "is_ICP": False, "points": 0},
            {"label": "$300K - $400K", "is_ICP": False, "points": 0},
            {"label": "More than $400K", "is_ICP": False, "points": 0},
        ])
    )
    model.add_features([feature_a, feature_b, feature_c])
    model.compute_normalized_weights()

    yield model


@fixture
def lead():
    """
    Yields a lead
    """
    yield {
        "Monthly Users": "100K - 200K",
        "Industry": "Technology",
        "Mkt Investment": "100k - $200K",
    }


@fixture
def feature_instances():
    feature_a = Feature(
        name="Monthly Users",
        weight=0.5,
        options_df=pd.DataFrame({
            'label': ['Up to 50K', '50K - 100K', '100K - 200K', 'More than 200K'],
            'is_ICP': [False, True, False, False],
            'points': [0, 0, 0, 0]
        })
    )

    feature_b = Feature(
        name="Industry",
        weight=0.25,
        options_df=pd.DataFrame([
            {"label": "Other", "is_ICP": False, "points": 0},
            {"label": "Agriculture", "is_ICP": False, "points": 0},
            {"label": "Transportation", "is_ICP": False, "points": 0},
            {"label": "Healthcare", "is_ICP": False, "points": 0},
            {"label": "Manufacturing", "is_ICP": False, "points": 0},
            {"label": "Education", "is_ICP": True, "points": 0},
            {"label": "Finance", "is_ICP": True, "points": 0},
            {"label": "Technology", "is_ICP": True, "points": 0},
            {"label": "Retail", "is_ICP": False, "points": 0},
            {"label": "Telecom", "is_ICP": False, "points": 0},
        ])
    )

    yield feature_a, feature_b


@fixture
def options_data_frame_instances():
    df_a = pd.DataFrame({
        'label': ['Up to 50K', '50K - 100K', '100K - 200K', 'More than 200K'],
        'is_ICP': [False, True, False, False],
        'points': [0, 50, 0, 0]
    })
    df_b = pd.DataFrame({
        'label': [df_a, 'Agriculture', 'Transportation'],
        'is_ICP': ['aaa', True, False],
        'points': ['aaa', 0, 0]
    })
    df_c = pd.DataFrame({
        'aaa': ['Other', 'Agriculture', 'Transportation'],
        'is_ICP': [False, True, False],
        'points': [0, 0, 0]
    })

    yield df_a, df_b, df_c
