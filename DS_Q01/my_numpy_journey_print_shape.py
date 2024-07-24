import numpy as np

def my_numpy_journey_print_shape(input):
    num_sublists = len(input)
    return (num_sublists,)
    # return np.array(input).shape


# array1 = [[1, 2, 3, 4, 5], [0,1,1,1,1]]
array1 = [[]]
print("Shape:", my_numpy_journey_print_shape(array1))