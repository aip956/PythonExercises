
import numpy as np

"""
Converts a Python list to a NumPy array
"""
def my_numpy_journey_two_d_array(arrays):
    try:
        np_array = np.array(arrays)
        print("NumPy array: ", np_array)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

arrays1 = [[1, 2, 3, 4, 5], [0,1,1,1,1]]
print("my_numpy_journey_two_d_array: ", my_numpy_journey_two_d_array(arrays1))