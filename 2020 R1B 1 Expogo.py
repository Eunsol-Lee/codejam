T = int(input())

for t in range(1, T + 1):
    X, Y = map(int, input().split())
    result = ''
    while X != 0 or Y != 0:
        print(X, Y, result)
        if (X + Y) % 2 == 0:
            result = 'IMPOSSIBLE'
            break
        if X % 2 == 1:
            if Y == 0:
                if X > 0:
                    result += 'E'
                    X -= 1
                else:
                    result += 'W'
                    X += 1
            else:
                if Y % 4 == 0 and (X + 1) % 4 == 2 or Y % 4 == 2 and (X + 1) % 4 == 0:
                    result += 'W'
                    X += 1
                else:
                    result += 'E'
                    X -= 1
        else:
            if X == 0:
                if Y > 0:
                    result += 'N'
                    Y -= 1
                else:
                    result += 'S'
                    Y += 1
            else:
                if X % 4 == 0 and (Y + 1) % 4 == 2 or X % 4 == 2 and (Y + 1) % 4 == 0:
                    result += 'S'
                    Y += 1
                else:
                    result += 'N'
                    Y -= 1
        X //= 2
        Y //= 2
    print('Case #{}: {}'.format(t, result))
