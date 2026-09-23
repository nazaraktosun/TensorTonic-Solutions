import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)

    if n < 2 :
        return {"variance": 0.0, "standart deviation": 0.0}

    x_bar = sum(x) / n
    sum_squared_diffs = sum((element - x_bar)**2 for element in x)


    variance = sum_squared_diffs / (n-1)

    std = variance**0.5
    return{
        "variance": float(variance),
        "standard_deviation":float(std)
    }
    