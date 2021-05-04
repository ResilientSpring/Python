from sklearn.base import BaseEstimator
from sklearn.base import ClassifierMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.base import clone
from sklearn.pipeline import _name_estimators
import numpy as np
import operator

class MajorityVoteClassifier(BaseEstimator, ClassifierMixin):
    """A majority vote ensemble classifier

    :parameter
    classifiers: array-like, shape = [n_classifiers]
        Different classifiers for the ensemble

    vote: str, {"classlabel", "probability"} (default="classlabel")



    """