from pytest import fixture
from glsm.non_predictive.model import NonPredictive
from glsm.non_predictive.features import Feature
import pandas as pd


@fixture
def non_predictive_model() -> NonPredictive:
    """
    Yields a NonPredictive() model with three features
    """
    model = NonPredictive()

    feature_a = Feature(
        name="Monthly Users",
        weight=0.5,
        points_map=[
            ["Up to 50K", 0],
            ["50K - 100K", 50],
            ["100K - 200K", 75],
            ["More than 200K", 100],
        ],
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
        points_map=[
            ["Other", 50 - (50 / 5) * 5],
            ["Agriculture", 50 - (50 / 5) * 4],
            ["Transportation", 50 - (50 / 5) * 3],
            ["Healthcare", 50 - (50 / 5) * 2],
            ["Manufacturing", 50 - (50 / 5)],
            ["Education", 50],
            ["Finance", 50],
            ["Technology", 50],
            ["Retail", 75],
            ["Telecom", 100],
        ],
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
        points_map=[
            ["Up to $50K", 50 - (50 / 2) * 2],
            ["50k - $100K", 50 - (50 / 2)],
            ["100k - $200K", 50],
            ["$200K - $300K", 50 + (50 / 3)],
            ["$300K - $400K", 50 + (50 / 3) * 2],  # 83.33333333333334
            ["More than $400K", 50 + (50 / 3) * 3],
        ],
        options_df=pd.DataFrame([
            {"label": "Up to $50K", "is_ICP": False, "points": 0},
            {"label": "50k - $100K", "is_ICP": False, "points": 0},
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

    lead = {
        "Monthly Users": "50K - 100K",
        "Industry": "Technology",
        "Mkt Investment": "$300K - $400K",
    }

    yield lead


@fixture
def feature_instances():
    feature_a = Feature(
        name="Monthly Users",
        weight=0.5,
        points_map=[
            ["Up to 50K", 0],
            ["50K - 100K", 50],
            ["100K - 200K", 75],
            ["More than 200K", 100],
        ],
        options_df=pd.DataFrame({
            'label': ['Up to 50K', '50K - 100K', '100K - 200K', 'More than 200K'],
            'is_ICP': [False, True, False, False],
            'points': [0, 0, 0, 0]
        })
    )

    feature_b = Feature(
        name="Industry",
        weight=0.25,
        points_map=[
            ["Other"],
            ["Agriculture"],
            ["Transportation"]
        ],
        options_df=pd.DataFrame({
            'label': ['Other', 'Agriculture', 'Transportation'],
            'is_ICP': [False, True, False],
            'points': [0, 0, 0]
        })
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
