T = int(input())

for t in range(1, T + 1):
    N = int(input())
    R = [0] * (N + 1)
    C = [0] * (N + 1)
    K = 0
    checkColumn = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(N):
        P = list(map(int, input().split()))
        K += P[i]
        check = [0] * (N + 1)
        for j in range(N):
            if check[P[j]]:
                R[i] = 1
            check[P[j]] = 1

            if checkColumn[j][P[j]]:
                C[j] = 1
            checkColumn[j][P[j]] = 1
    rCount = sum(R)
    cCount = sum(C)
    print('Case #{}: {} {} {}'.format(t, K, rCount, cCount))
