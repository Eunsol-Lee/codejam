T = int(input())

for t in range(1, T + 1):
    X, Y, M = input().split()
    X = int(X)
    Y = int(Y)
    result = "IMPOSSIBLE"
    for i in range(len(M)):
        x = M[i]
        if x == 'N':
            Y += 1
        if x == 'S':
            Y -= 1
        if x == 'E':
            X += 1
        if x == 'W':
            X -= 1
        if (abs(X) + abs(Y)) <= i + 1:
            result = str(i + 1)
            break
    print('Case #{}: {}'.format(t, result))
