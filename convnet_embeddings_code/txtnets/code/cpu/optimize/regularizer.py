__author__ = 'mdenil'

import numpy as np

import generic.optimize.regularizer


class L2Regularizer(generic.optimize.regularizer.L2Regularizer):
    def _sum(self, X):
        return np.sum(X)