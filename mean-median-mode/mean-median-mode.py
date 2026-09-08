from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)
    mod = {}
    for item in x:
        mod[item] = mod.get(item,0) + 1
    mod_value = max(mod,key = mod.get)
        
    return {"mean" : float(mean),
            "median" : float(median),
            "mode": float(mod_value)}