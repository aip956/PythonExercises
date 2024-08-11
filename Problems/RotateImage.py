# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


def rotate(matrix):
    """
    Function to rotate the matrix by 90 degrees
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        print("i: ", i)
        for j in range(i, n):
            print("j: ", j)
            print("matrix[i][j]", matrix[i][j])
            print("matrix[j][i]", matrix[j][i])
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print("17matrix: ", matrix)
    print("Trpsd: ", matrix)
    
    # Reverse each row
    for row in matrix:
        row.reverse()
    print("21Reversed: ", matrix)
    return matrix

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# rotate(matrix1)

matrix2 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
    ]
rotate(matrix2)