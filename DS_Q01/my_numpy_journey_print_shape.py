import numpy as np

def my_numpy_journey_print_shape(input):
    input_array = np.array(input)
    print ((input_array.shape[0],))

array1 = [[1, 2, 3, 4, 5], [0,1,1,1,1]]
# array1 = [[]]
my_numpy_journey_print_shape(array1)
# print("Shape:", my_numpy_journey_print_shape(array1))