T = int(input())

for t in range(1, T + 1):
    R, C = map(int, input().split())
    reverse = 0
    result = "POSSIBLE"
    resultList = []
    if R > C:
        reverse = 1
        R, C = C, R
    if R == 2:
        if C < 5:
            result = "IMPOSSIBLE"
        else:
            oneCount = C - 2
            twoCount = C
            for x in range(1, R * C + 1):
                if x % 2 == 1:
                    resultList.append([1, oneCount])
                    oneCount -= 1
                    if oneCount == 0:
                        oneCount = C
                else:
                    resultList.append([2, twoCount])
                    twoCount -= 1
    if R >= 3:
        if R == 3 and C == 3:
            result = "IMPOSSIBLE"
        else:
            oneCount = 1
            twoCount = 3
            rCount = 1
            for x in range(1, R * C + 1):
                if rCount % 2 == 1:
                    resultList.append([rCount, oneCount])
                else:
                    resultList.append([rCount, twoCount])
                rCount += 1
                if rCount == R + 1:
                    oneCount += 1
                    twoCount += 1
                    if twoCount == C + 1:
                        twoCount = 1
                    rCount = 1
        if R == C and R % 2 == 0:
            temp = resultList[R * C - C]
            for i in range(R * C - C, R * C - 1):
                resultList[i] = resultList[i + 1]
            resultList[R * C - 1] = temp
    print('Case #{}: {}'.format(t, result))
    if result == "POSSIBLE":
        for x in resultList:
            if reverse == 0:
                print('{} {}'.format(x[0], x[1]))
            else:
                print('{} {}'.format(x[1], x[0]))

        # for x in range(len(resultList) - 1):
        #     if resultList[x][0] == resultList[x + 1][0] or resultList[x][1] == resultList[x + 1][1] or resultList[x][0] + resultList[x][1] == resultList[x+1][0] + resultList[x+1][1] or resultList[x][0] + resultList[x][1] == resultList[x-1][0] + resultList[x-1][1]:
        #         print('wrong', resultList[x])
        #         print('wrong', resultList[x+1])
