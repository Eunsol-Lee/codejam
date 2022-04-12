T = int(input())

for t in range(1, T + 1):
    S = input()
    result = ''
    for x in S:
        result += int(x) * '(' + x + int(x) * ')'
    for _ in range(9):
        result = result.replace(')(', '')
    print('Case #{}: {}'.format(t, result))
