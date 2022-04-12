T = int(input())

for t in range(1, T + 1):
    stringCount = [{} for _ in range(10)]
    totalCount = {}
    totalString = {}
    resultString = ''
    exceptionFlag = False
    U = int(input())
    for _ in range(10000):
        Q, R = input().split()
        if Q == '-1':
            exceptionFlag = True
        if len(R) == U:
            key = R[0]
            if not key in totalCount:
                totalCount[key] = 1
            else:
                totalCount[key] += 1

        if len(Q) == len(R):
            key = int(Q[0])
            if R[0] in stringCount[key]:
                stringCount[key][R[0]] += 1
            else:
                stringCount[key][R[0]] = 1
        for x in R:
            if not x in totalString:
                totalString[x] = True

    for key in stringCount[9]:
        totalString[key] = False
    for key in totalString:
        if totalString[key]:
            resultString += key
    for i in range(1, 10):
        for key in stringCount[i]:
            if not totalString[key]:
                resultString += key
                totalString[key] = True

    # if exceptionFlag:
    resultString = ''
    # print(totalCount)
    for i in range(1, 10):
        maxValue = 0
        maxKey = ''
        for key in totalCount:
            if totalCount[key] > maxValue:
                maxValue = totalCount[key]
                maxKey = key
        resultString += maxKey
        totalCount[maxKey] = 0
    for key in totalString:
        if not key in totalCount:
            resultString = key + resultString
    print('Case #{}: {}'.format(t, resultString))
