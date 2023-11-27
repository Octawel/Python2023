def spiral_order(matrix):
    if not matrix:
        return ""
    
    rows, cols = len(matrix), len(matrix[0])
    result = []

    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        #left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])

        #top to bottom
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])

        #right to left
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][i])

        #bottom to top
        if left < right:
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    return ''.join(result)

matrix = [
    ["f", "i", "r", "s"],
    ["n", "_", "l", "t"],
    ["o", "b", "a", "_"],
    ["h", "t", "y", "p"]
]

result = spiral_order(matrix)
print(result)
