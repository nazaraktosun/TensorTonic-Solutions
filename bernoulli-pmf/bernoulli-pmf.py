import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x_arr = np.array(x)
    pmf_array = np.where(x_arr ==1,p,1-p) #np.where condition,value if true value if false
    mean = float(p)
    variance = float(p*(1-p))
    
    return {
        "pmf" : pmf_array,
        "mean" : mean,
        "variance" : variance
    }