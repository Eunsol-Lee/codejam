# It is too slow for N > 10

T = int(input())


def findTrace(N, K, array, index, count):
    if index == N:
        if count != K:
            return False
        if array[1] == array[N - 1] and array[0] != array[1] or array[0] == array[N - 2] and array[N - 1] != array[N - 2]:
            return False
        return True

    left = 1 if index == 0 else array[index - 1]
    left = max(left, K - count - N * (N - index - 1))
    right = N
    for x in range(left, right + 1):
        array[index] = x
        result = findTrace(N, K, array, index + 1, count + x)
        if result == False:
            array[index] = 0
        if array[N - 1] and result:
            return True
    return False


def findValueByPosition(matrix, rows, columns, index, row, N):
    if row == N:
        return True
    if rows[row] == 1:
        result = findValueByPosition(matrix, rows, columns, index, row + 1, N)
        return result
    else:
        for i in range(N):
            if not columns[i] and matrix[row][i] == 0:
                matrix[row][i] = index
                columns[i] = 1
                result = findValueByPosition(
                    matrix, rows, columns, index, row + 1, N)
                if result == True:
                    return True
                matrix[row][i] = 0
                columns[i] = 0
        return False


def findValueByIndex(matrix, final, N):

    for i in range(N):
        columns = [0] * N
        rows = [0] * N
        for j in range(N):
            for k in range(N):
                if matrix[j][k] == final[i]:
                    columns[k] = 1
                    rows[j] = 1
        findValueByPosition(matrix, rows, columns, final[i], 0, N)


for t in range(1, T + 1):
    N, K = map(int, input().split())
    trace = [0] * N
    if N == 3 and K % 3 == 0:
        trace = [K // 3] * N
    else:
        findTrace(N, K, trace, 0, 0)
    if trace[N - 1]:
        print('Case #{}: {}'.format(t, "POSSIBLE"))
        matrix = [[0] * N for _ in range(N)]
        count = [[0, 0] for _ in range(N)]
        for i in range(N):
            matrix[i][i] = trace[i]
            count[trace[i] - 1][0] += 1
            count[i][1] = i + 1
        count = sorted(count, reverse=True)
        final = []
        for i in range(N):
            final.append(count[i][1])
        findValueByIndex(matrix, final, N)
        for i in range(N):
            print(' '.join(map(str, matrix[i])))
    else:
