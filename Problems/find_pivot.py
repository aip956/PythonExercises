"""
Given an array of integers and its size passed as parameters,
create a function able to return the pivot index of this array.
The pivot index is the index where the sum of the numbers on the left
is equal to the sum of the numbers on the right.

If there is no pivot present, return -1.

int	find_pivot(int *arr, int n);
If there is no pivot present, return -1.
Input: [1, 2, 3, 4, 0, 6] && 6
Output: 3
sum from_left and from_right, index from_left and from_right
while 
if from_left_sum < from_right_sum, increment from_left_index_index
else if from_left > from_right, decriment from_right_index
else if equal, increment and decriment both indices and sums

"""

def find_pivot(param_1, param_2):
    from_left_index = 0
    from_right_index = param_2 - 1
    from_left_sum = param_1[0]
    from_right_sum = param_1[param_2 - 1]
    while from_right_index - from_left_index > 2:
        if from_left_sum < from_right_sum:
            from_left_index += 1
            from_left_sum += param_1[from_left_index]
        elif from_left_sum > from_right_sum:
            from_right_index -= 1
            from_right_sum += param_1[from_right_index]
        elif from_left_sum == from_right_sum:
            if from_right_index - from_left_index == 2:
                return from_left_index + 1
            from_left_index += 1
            from_left_sum += param_1[from_left_index]
            from_right_index -= 1
            from_right_sum += param_1[from_right_index]
    return -1
        
param_1 = [1, 2, 3, 4, 0, 6]
param_2 = 6       
print(find_pivot(param_1, param_2))