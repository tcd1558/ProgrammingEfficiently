
import numpy as np
import mandel

def compute_mandel_vec(cs, maxit=256):
    return np.array([mandel.compute_mandel(c, maxit) for c in cs])
