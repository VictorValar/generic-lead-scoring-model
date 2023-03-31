from pytest import fixture
from glsm.non_predictive import NonPredictive
from glsm.features import Feature

@fixture
def non_predictive_model() -> NonPredictive:
    '''
    Instanciates a non predictive model with three features
    '''
    model = NonPredictive()

    feature_a = Feature(
        name="Monthly Users",
        weight=0.5,
        points_map=[
            ("Up to 50K",00),
            ("50K - 100K",50),
            ("100K - 200K",70),
            ("More than 200K",100),
        ]
    )
    model.add_feature(feature_a)

    feature_b = Feature(
        name="Industry",
        weight=0.25,
        points_map=[
            ("Technology",70),
            ("Real State",20),
            ("Retail",50),
            ("Education",50),
            ("Health",100),
        ]
    )
    model.add_feature(feature_b)

    feature_c = Feature(
        name="Mkt Investment",
        weight=1,
        points_map=[
            ("Up to $50K",0),
            ("50k - $100K",30),
            ("100k - $200K",50),
            ("$200K - $300K",70),
            ("$300K - $400K",90),
            ("More than $400K",100),
        ]
    )
    model.add_feature(feature_c)

    model.compute_normalized_weights()

    yield model


@fixture
def lead():
    '''
    Instanciates a lead
    '''
    lead = {
        "Monthly Users": "50K - 100K",
        "Industry": "Retail",
        "Mkt Investment": "100k - $200K",
    }
    yield lead