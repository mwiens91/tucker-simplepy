#!/usr/bin/env python3

import numpy as np
from tucker_simplepy.tableau import Tableau


m = np.matrix([[1, 2], [3, 4], [5, 6]])
t = Tableau(m)

print(t.m, t.n)

b = t.pivot(1, 1)

print(b)
