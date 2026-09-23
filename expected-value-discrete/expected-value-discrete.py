import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x_arr = np.array(x)
    p_arr = np.array(p)

    expected_value = np.sum(x_arr*p_arr)
    return float(expected_value)