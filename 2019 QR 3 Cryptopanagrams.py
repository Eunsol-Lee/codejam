from math import sqrt

T = int(input())


def GCD(a, b):
    maxValue = max(a, b)
    minValue = min(a, b)
    if minValue == 0:
        return maxValue
    else:
        return GCD(maxValue % minValue, minValue)


def findValue(n):
    if n == L:
        return
    if numbers[n] == 0:
        if multiple[n] == multiple[n + 1]:
            findValue(n + 1)
            numbers[n] = multiple[n] // numbers[n + 1]
        else:
            numbers[n + 1] = GCD(multiple[n], multiple[n + 1])
            numbers[n] = multiple[n] // numbers[n + 1]
            findValue(n + 1)
    else:
        numbers[n + 1] = multiple[n] // numbers[n]
        findValue(n + 1)


for t in range(1, T + 1):
    N, L = map(int, input().split())
    multiple = list(map(int, input().split()))
    numbers = [0] * (L + 1)
    maps = {}
    result = ''

    findValue(0)

    uniqueNumbers = list(set(numbers))
    uniqueNumbers.sort()
    for i in range(len(uniqueNumbers)):
        maps[uniqueNumbers[i]] = chr(65 + i)
    for x in numbers:
        result += maps[x]

    print('Case #{}: {}'.format(t, result))
