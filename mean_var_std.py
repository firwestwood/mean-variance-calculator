# mean_var_std.py
import numpy as np

def calculate(numbers):
    # Check if the list has exactly 9 elements
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to a 3x3 Numpy array
    matrix = np.array(numbers).reshape(3, 3)
    
    # Calculate metrics for both axes and flattened
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    
    return calculations