import numpy as np

def my_numpy_journey_sum(input1):
    sum = np.sum(input1)
    print("Sum: ", sum)
    return sum

input1 = [[1, 2], [3, 4]]
input2 = [[5, 6], [7, 8]]
my_numpy_journey_sum(input1)
my_numpy_journey_sum(input2)