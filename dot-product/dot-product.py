import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
  
    dot_product = np.array(x)@np.array(y)
    return float(dot_product)
    