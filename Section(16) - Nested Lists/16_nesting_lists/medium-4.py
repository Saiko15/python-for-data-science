def read_matrix():
    rows = int(input())
    matrix = [0] * rows

    for row in range(rows):
        matrix[row] = list(map(int, input().split()))

    return rows, len(matrix), matrix

def is_inside(i, j):
    return i <= matrix and j <= matrix[0]

if __name__ == '__main__':

    rows, cols, matrix= read_matrix()

    di = [0, 1, 1]
    dj = [1, 0, 1]

    sr, sc = 0, 0

    for i in matrix:
        for j in i:
            if is_inside():
                break