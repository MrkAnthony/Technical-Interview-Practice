matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

res = []

l, r = 0, len(matrix[0])
top, bottom = 0, len(matrix)

while l < r and top < bottom:

    for i in range(l, r):
        res.append(matrix[top][i])
    top += 1

    for i in range(top, bottom):
        res.append(matrix[i][r - 1])
    r -= 1

    if not (l < r and top < bottom):
        break

    for i in range(r - 1, l - 1, -1):
        res.append(matrix[bottom - 1][i])
    bottom -= 1

matrix_2D = [
    [4, 8, 12],
    [16, 20, 24],
    [28, 32, 36],
    [40, 44, 48]
]


def find_target(matrix, target):
    seen = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            seen.add(matrix[i][j])

    if target in seen:
        return True
    return False


strs = ["357", "248", "139"]
strs2 = ["111", "222", "333"]
strs3 = ["123", "234", "345"]


def find_increasing_col(strs):
    cnt = 0
    for col in range(len(strs[0])):
        for row in range(1, len(strs)):
            if strs[row][col] > strs[row - 1][col]:
                cnt += 1
                break
    return cnt


print(find_increasing_col(strs))
print(find_increasing_col(strs2))
print(find_increasing_col(strs3))
