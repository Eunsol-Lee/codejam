bw = [32, 16, 8, 4, 2, 1]
sample = []
for x in bw:
    sample.append((('0' * (x // 2)) + ('1' * (x // 2))) * (1024 // x) + '0')

T = int(input())


def divideAndConquer(st, en, or_st, depth):
    if st == en:
        output = ''
        for x in range(or_st, or_st + bw[depth]):
            output += str(x) + ' '
        return output
    if depth == 5:
        return ''
    count = [0, 0]
    for x in range(st, en):
        count[int(Res[depth][x])] += 1
    output = ''
    output += divideAndConquer(st, st + count[0], or_st, depth + 1)
    output += divideAndConquer(st + count[0],
                               en, or_st + bw[depth + 1], depth + 1)
    return output


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
        output += divideAndConquer(i, ns, original, 0)
        i = ns
        original += 32
    print(output)
    response = input()
