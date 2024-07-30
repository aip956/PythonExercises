import numpy as np

"""
Converts a Python list to a NumPy array
"""
def my_numpy_journey_one_d_array(array):
    try:
        np_array = np.array(array)
        print("NumPy array: ", np_array)
        return True
    except Exception as e:
        return False

print("my_numpy_journey_one_d_array([1, 2, 3, 4, 5]): ", my_numpy_journey_one_d_array([1, 2, 3, 4, 5]))