from pytest import fixture
from glsm.non_predictive import NonPredictive
from glsm.features import Feature

@fixture
def non_predictive_model() -> NonPredictive:
    '''
    Yields a NonPredictive() model with three features
    '''
    model = NonPredictive()

    feature_a = Feature(
        name="Monthly Users",
        weight=0.5,
        points_map=[
            ("Up to 50K",0),
            ("50K - 100K",50),
            ("100K - 200K",75),
            ("More than 200K",100),
        ]
    )

    feature_b = Feature(
        name="Industry",
        weight=0.25,
        points_map=[
            ("Other",50 - 50/5*5),
            ("Agriculture",50 - 50/5*4),
            ("Transportation",50 - 50/5*3),
            ("Healthcare",50 - 50/5*2),
            ("Manufacturing",50 - 50/5),
            ("Education",50),
            ("Finance",50),
            ("Technology",50),
            ("Retail",75),
            ("Telecom",100),
        ]

    )

    feature_c = Feature(
        name="Mkt Investment",
        weight=1,
        points_map=[
            ("Up to $50K",50-50/2*2),
            ("50k - $100K",50-50/2),
            ("100k - $200K",50),
            ("$200K - $300K",50 + 50/3),
            ("$300K - $400K",50 + 50/3*2),
            ("More than $400K",50 + 50/3*3),
        ]
    )
    model.add_features([feature_a, feature_b, feature_c])

    model.compute_normalized_weights()

    yield model

@fixture
def lead():
    '''
    Yields a lead
    '''

    lead = { # lambda = 81.43
        "Monthly Users": "50K - 100K",
        "Industry": "Technology",
        "Mkt Investment": "$300K - $400K",
    }

    yield lead


