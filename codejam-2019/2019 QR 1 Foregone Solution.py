T = int(input())

for t in range(1, T + 1):
    N = input()
    X = ''
    Y = ''
    for x in N:
        if x == '4':
            X += '2'
            Y += '2'
        else:
            X += x
            Y += '0'
    # print(f'Case #{t}: {int(X)} {int(Y)}')
    print('Case #{}: {} {}'.format(t, X, Y))
