T = int(input())
for t in range(1, T + 1):
    N = int(input())
    P = input()
    result = ''
    for x in P:
        result += 'E' if x == 'S' else 'S'
    print('Case #%d: %s' % (t, result))
