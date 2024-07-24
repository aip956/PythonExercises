import numpy as np

# def my_numpy_journey_print_datatype(input):
    
#     np_input = np.array(input, dtype=str)
#     print("Data type: ", np.array(np_input).dtype)
#     return np.array(input).dtype


def my_numpy_journey_print_datatype(input_list):
    # Convert the entire input list to a string representation
    input_str = str(input_list)
    
    # Create a NumPy array from this string, ensuring it's treated as a single element array of strings
    np_input = np.array([input_str])
    
    # Print the dtype of the resulting array
    print("Data: ", np_input.dtype)
    
    return np_input.dtype

# # print(my_numpy_journey_print_datatype([[]]))
# # print(my_numpy_journey_print_datatype([[1, 2, 3, 4], [0, 1, 1, 1], [7, 7, 7, 7]]))
my_numpy_journey_print_datatype(([[]]))
my_numpy_journey_print_datatype([[1, 2, 3, 4], [0, 1, 1, 1], [7, 7, 7, 7]])