from pytest import fixture
from glsm.non_predictive import NonPredictive
from glsm.features import Feature

@fixture
def non_predictive_model() -> NonPredictive:
    '''
    Instanciates a non predictive model
    '''
    model = NonPredictive()

    map = [
        ("Up to 50K",00),
        ("50K - 100K",50),
        ("100K - 200K",70),
        ("More than 200K",100),
    ]

    feature = Feature(name="test_feature", points_map=map)

    model.add_feature(feature)

    yield model