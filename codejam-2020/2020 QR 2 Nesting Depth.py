T = int(input())

for t in range(1, T + 1):
    S = input() + '0'
    d = 0
    result = ''
    for x in S:
        current = int(x)
        if current > d:
            result += '(' * (current - d)
            d = current
        if current < d:
            result += ')' * (d - current)
            d = current
        result += x
    result = result[:-1]
    print('case #{}: {}'.format(t, result))
