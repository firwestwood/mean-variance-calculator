# main.py
from mean_var_std import calculate

# Example input to test the function
try:
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
except ValueError as e:
    print(e)

# Import and run tests from test_module.py
import test_module
