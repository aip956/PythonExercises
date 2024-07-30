import numpy as np

def my_numpy_journey_sort(input):
    np_array = np.array(input)
    np_array.sort()
    print("Sorted array: ", np_array)
    return np_array

array1 = [4, 2, 1, 7]
my_numpy_journey_sort(array1)
