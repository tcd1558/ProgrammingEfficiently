
import numpy as np

def compute_mandel(c, maxit=256):
    z = 0.0j

    for it in range(1, maxit):
        z = z*z + c
        
        if abs(z) > 2.0:
            return it

    return np.inf
