import numpy as np

def my_numpy_journey_add(input1, input2):
    np_array1 = np.array(input1)
    np_array2 = np.array(input2)
    np_array = np.add(np_array1, np_array2)
    print("Array: ", np_array)
    return np_array

input1 = [[1, 2], [3, 4]]
input2 = [[5, 6], [7, 8]]
my_numpy_journey_add(input1, input2)