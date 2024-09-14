"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted from left_ind to right_ind.
The first integer of each row is greater than the last integer of the previous row.
 Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Calc middle index
Map the 1d index to 2d index
Binary search
"""

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    print("m: ", m) # num of rows
    print("n: ", n) # num of columns

    left_ind, right_ind = 0, m * n - 1
    print("23left_ind: ", left_ind)
    print("24right_ind: ", right_ind)
    while left_ind <= right_ind:
        print("26left_ind: ", left_ind)
        print("27right_ind: ", right_ind)
        mid_ind = (left_ind + right_ind) // 2 # middle index
        print("29mid_ind: ", mid_ind)
        mid_val = matrix[mid_ind // n][mid_ind % n] # value at middle index
        print("31mid_val: ", mid_val)
        if mid_val == target:
            return True
        elif mid_val < target:
            left_ind = mid_ind + 1
            print("36left_ind: ", left_ind)
            print("37mid_ind: ", mid_ind)
        else:
            right_ind = mid_ind - 1
            print("40right_ind: ", right_ind)
            print("41mid_ind: ", mid_ind)
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 13
print(searchMatrix(matrix1, target1))
