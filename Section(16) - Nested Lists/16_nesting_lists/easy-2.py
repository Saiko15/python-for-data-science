def read_matrix():
    rows = int(input())
    matrix = [0] * rows

    for row in range(rows):
        matrix[row] = list(map(int, input().split()))

    return rows, len(matrix), matrix

if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    lower = []
    idx = 0
    for j in range(cols):
        for i in range(idx, rows):
            lower.append(matrix[i][j])
        idx += 1

    print(sum(lower))

    upper= []
    idx = 0
    for i in range(rows):
        for j in range(idx, cols):
            upper.append(matrix[i][j])
        idx += 1

    print(sum(upper))