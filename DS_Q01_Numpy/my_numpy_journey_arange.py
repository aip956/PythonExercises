import numpy as np

def my_numpy_journey_arange(start, stop, step):
    np_array = np.arange(start, stop, step)
    print("Array: ", np_array)
    return np_array

my_numpy_journey_arange(1, 10, 2)