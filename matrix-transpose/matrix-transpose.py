import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    if not A or not A[0]:
            return np.array([])

    M = len(A)          # Original rows
    N = len(A[0])       # Original columns
    
    # Initialize result matrix of shape (N, M) filled with zeros
    result = [[0] * M for _ in range(N)]
    
    # Manual indexing loops
    for i in range(M):
        for j in range(N):
            result[j][i] = A[i][j]  # Swap row and column indices
            
    return np.array(result)
