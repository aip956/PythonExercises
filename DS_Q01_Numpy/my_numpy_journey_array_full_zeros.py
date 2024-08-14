import numpy as np

def my_numpy_journey_array_full_zeros(shape):
    try:
        np_array = np.zeros(shape)
        print("NumPy array: ", np_array)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    
print("my_numpy_journey_array_full_zeros(5): ", my_numpy_journey_array_full_zeros(5))