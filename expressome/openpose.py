from tfopenpose.estimator import TfPoseEstimator
from tfopenpose.networks import get_graph_path

import logsharing
log = logsharing.get_logger()

def load_estimator():
    print('load_estimator')
    path = get_graph_path('cmu')
    log.info('CMU graph at path: %s', path)
    return TfPoseEstimator(path)
