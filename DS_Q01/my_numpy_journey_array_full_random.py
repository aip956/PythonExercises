import numpy as np

def my_numpy_journey_array_full_random(dim1, dim2):
    np_array = np.random.rand(dim1, dim2)
    print("Array: ", np_array)
    return np_array


my_numpy_journey_array_full_random(3, 4)