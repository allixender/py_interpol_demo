# -*- coding: utf-8 -*-
import numpy as np
from scipy.interpolate import Rbf


def scipy_idw(x, y, z, xi, yi):
    interp = Rbf(x, y, z, function='linear')
    return interp(xi, yi)

