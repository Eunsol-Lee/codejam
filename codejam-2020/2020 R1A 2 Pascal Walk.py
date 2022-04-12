T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = []
    if N <= 30:
        for i in range(1, N + 1):
            result.append([i, 1])
    else:
        binary = N - 30
        binaryString = bin(binary)[2:][::-1]
        positionStart = True
        count = 0
        for i in range(len(binaryString)):
            if binaryString[i] == '1':
                if positionStart:
                    for j in range(i + 1):
                        result.append([i + 1, j + 1])
                else:
                    for j in range(i, -1, -1):
                        result.append([i + 1, j + 1])
                positionStart = not positionStart
            else:
                if positionStart:
                    result.append([i + 1, 1])
                else:
                    result.append([i + 1, i + 1])
                count += 1
        for i in range(len(binaryString), len(binaryString) + 30 - count):
            if positionStart:
                result.append([i + 1, 1])
            else:
                result.append([i + 1, i + 1])
    print('Case #{}:'.format(t))
    count = 0
    for x in result:
        print(x[0], x[1])
