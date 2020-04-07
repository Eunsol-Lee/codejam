T = int(input())


def findTrace(N, K, trace):
    if (N == 2 or N == 3) and K % N != 0:
        return "IMPOSSIBLE"
    if K % N == 0:
        for _ in range(N):
            trace.append(K // N)
        return "POSSIBLE"

    for x in range(1, N + 1):
        for y in range(x, N + 1):
            if (K - x - y) % (N - 2) == 0:
                z = (K - x - y) // (N - 2)
                if z != x and z != y and z >= 1 and z <= N:
                    for _ in range(N - 2):
                        trace.append(z)
                    trace.append(x)
                    trace.append(y)
                    return "POSSIBLE"
    return "IMPOSSIBLE"


def findLastTwo(matrix, checkRow, checkColumn, r, c):
    if r == len(matrix):
        return True
    for i in range(1, len(matrix) + 1):
        if not checkRow[r][i] and not checkColumn[c][i]:
            matrix[r][c] = i
            checkRow[r][i] = True
            checkColumn[c][i] = True
            if c == len(matrix) - 3:
                result = findLastTwo(matrix, checkRow, checkColumn, r + 1, 0)
                if result:
                    return True
            else:
                result = findLastTwo(matrix, checkRow, checkColumn, r, c + 1)
                if result:
                    return True
            checkRow[r][i] = False
            checkColumn[c][i] = False
    return False


def findMatrix(N, K, trace, matrix):
    if trace[N - 1] == trace[N - 2]:
        if trace[N - 1] == trace[0]:
            for i in range(N):
                count = trace[i]
                for j in range(i, N + i):
                    matrix[i][j % N] = (count - 1) % N + 1
                    count += 1
            return
        else:
            for i in range(N):
                matrix[i][i] = trace[i]
                if i < N - 3:
                    matrix[i][i + 1] = trace[N - 1]
                else:
                    if i == N - 3:
                        matrix[i][0] = trace[N - 1]
            matrix[N - 2][N - 1] = matrix[N - 1][N - 2] = trace[0]

            numbers = []
            for i in range(1, N + 1):
                if i != trace[0] and i != trace[N - 1]:
                    numbers.append(i)

            for i in range(N - 2):
                count = 0
                for j in range(i + 2, 2 * N + 2):
                    if matrix[i][j % N] == 0:
                        matrix[i][j % N] = numbers[count]
                        count += 1

            checkColumn = [[False] * (N + 1) for _ in range(N - 2)]
            checkRow = [[False] * (N + 1) for _ in range(N)]

            for i in range(N - 2):
                for j in range(N - 2):
                    checkColumn[j][matrix[i][j]] = True

            for i in range(N - 2, N):
                checkRow[i][trace[0]] = True
                checkRow[i][trace[N - 1]] = True

            findLastTwo(matrix, checkRow, checkColumn, N - 2, 0)

            return
    else:
        order = []
        order.append(trace[0])
        order.append(trace[N - 2])
        order.append(trace[N - 1])
        for i in range(1, N + 1):
            if i != order[0] and i != order[1] and i != order[2]:
                order.append(i)

        for i in range(N - 2):
            count = 0
            for j in range(i, 2 * N):
                position = j % N
                if matrix[i][position] == 0 and not (position == N - 2 and order[count] == trace[N - 2]) and not (position == N - 1 and order[count] == trace[N - 1]):
                    matrix[i][position] = order[count]
                    count += 1

        matrix[N - 2][N - 2] = trace[N - 2]
        matrix[N - 1][N - 1] = trace[N - 1]
        matrix[N - 2][N - 1] = trace[0]
        matrix[N - 1][N - 2] = trace[0]

        checkColumn = [[False] * (N + 1) for _ in range(N - 2)]
        checkRow = [[False] * (N + 1) for _ in range(N)]

        for i in range(N - 2):
            for j in range(N - 2):
                checkColumn[j][matrix[i][j]] = True

        for i in range(N - 2, N):
            checkRow[i][matrix[i][N - 2]] = True
            checkRow[i][matrix[i][N - 1]] = True

        findLastTwo(matrix, checkRow, checkColumn, N - 2, 0)

        return


for t in range(1, T + 1):
    N, K = map(int, input().split())
    trace = []

    result = findTrace(N, K, trace)
    print('Case #{}: {}'.format(t, result))
    if result == "POSSIBLE":
        matrix = [[0] * N for _ in range(N)]
        findMatrix(N, K, trace, matrix)
        for i in range(N):
            print(' '.join(map(str, matrix[i])))
