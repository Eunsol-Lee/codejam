T = int(input())

for t in range(1, T + 1):
    N, D = map(int, input().split())
    dString = list(map(int, input().split()))
    dString.sort()
    baseMap = {}
    bonusMap = {}
    countMap = {}
    for x in dString:
        for j in range(1, D + 1):
            key = x // j
            # if key != 0:
            #     if not key in countMap:
            #         countMap[key] = x // key
            #     else:
            #         countMap[key] += x // key
            if key and x % key == 0 and x // key <= D:

                if j == 1:
                    if not key in baseMap:
                        baseMap[key] = 1
                    else:
                        baseMap[key] += 1
                else:
                    if not key in bonusMap:
                        bonusMap[key] = 1
                    else:
                        bonusMap[key] += 1

    totalKeys = set().union(baseMap, bonusMap)
    maxKey = 1
    maxValue = 0
    # print(baseMap, bonusMap, countMap)

    results = {}
    for key in totalKeys:
        bonusValue = 0
        if key in baseMap:
            bonusValue = baseMap[key]
        if key in bonusMap:
            rest = D - bonusValue
            if rest >= 2 * bonusMap[key]:
                bonusValue += bonusMap[key]
            else:
                bonusValue += rest // 2
        results[key] = bonusValue

    for key in sorted(results, key=results.get, reverse=True):
        value = results[key]
        count = 0

        for x in dString:
            count += x // key
            if count > D:
                break

        print(key, value, count)

        if count >= D and value > maxValue:
            maxValue = value
        # if count < D:

    print('Case #{}: {}'.format(t, D - maxValue))
