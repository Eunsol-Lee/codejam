bw = [32, 16, 8, 4, 2, 1]
sample = []
for x in bw:
    sample.append((('0' * (x // 2)) + ('1' * (x // 2))) * (1024 // x) + '0')

T = int(input())


def findNumber(st, en, or_st):
    check = [0] * 32
    for x in range(st, en):
        value = 0
        for i in range(5):
            value += int(Res[i][x]) * bw[i + 1]
        check[value] = 1
    result = ''
    for x in range(32):
        if check[x] == 0:
            result += str(x + or_st) + ' '
    return result


for t in range(1, T + 1):
    N, B, F = map(int, input().split())
    Res = []
    for i in range(0, 5):
        print(sample[i][:N])
        Res.append(input() + sample[i][N:])
    i = 0
    original = 0
    output = ''
    while original < 1024:
        ns = Res[0].find('0', i + 16)
        output += findNumber(i, ns, original)
        i = ns
        original += 32
    print(output)
    response = input()
