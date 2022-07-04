def read_matrix():
    rows = int(input())
    matrix = [0] * rows

    for row in range(rows):
        matrix[row] = list(map(int, input().split()))

    return matrix

def swap_col(col1, col2):

    matrix = read_matrix()
    for row in range(len(matrix)):
        matrix[row][col1] , matrix[row][col2] = matrix[row][col2], matrix[row][col1] 

    return matrix

if __name__ == '__main__':

    print(swap_col(0, 3))