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

Right way:
create a total sum; (16)
create a left_sum (0, 1, 3, 6, 10, 10)
right_sum = total_sum - left_sum - arr[i] ( 15, 13, 10, 6, 0)
when left_sum == right_sum, return index + 1

"""

def find_pivot(param_1, param_2):
    total_sum = sum(param_1)
    left_sum = 0
    for i in range(param_2):
        right_sum = total_sum - left_sum - param_1[i]
        print(f"left_sum: {left_sum}, right_sum: {right_sum}")
        if left_sum == right_sum:
            return i
        left_sum += param_1[i]
    return -1

param_1 = [1, 2, 3, 4, 0, 6]
param_2 = 6       
print(find_pivot(param_1, param_2))