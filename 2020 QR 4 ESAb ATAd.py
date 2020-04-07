T, B = map(int, input().split())


def getResult(a, b):
    print(a + 1)
    first = int(input())
    print(b + 1)
    second = int(input())
    return first, second


def writeData(array, index, value, toggle, reverse):
    if reverse:
        index = len(array) - index - 1
    if toggle:
        value = 1 - value
    array[index] = value


for t in range(1, T + 1):
    left = 0
    toggle = False
    reverse = False
    result = [0] * B
    toggleIndex = -1
    reverseIndex = -1
    for i in range(0, 150, 2):
        if i % 10 == 0 and i != 0:
            toggle = False
            reverse = False
            if toggleIndex != -1 and reverseIndex != -1:
                p, q = getResult(toggleIndex, reverseIndex)
                if p != result[toggleIndex]:
                    toggle = True
                if q != result[reverseIndex] and not toggle or q == result[reverseIndex] and toggle:
                    reverse = True
            else:
                if toggleIndex != -1:
                    p, q = getResult(toggleIndex, B - 1)
                    if p != result[toggleIndex]:
                        toggle = True
                else:
                    p, q = getResult(reverseIndex, B - 1)
                    if p != result[reverseIndex]:
                        reverse = True

        else:
            p, q = getResult(left, B - 1 - left)
            writeData(result, left, p, toggle, reverse)
            writeData(result, B - 1 - left, q, toggle, reverse)
            if toggleIndex == -1 and p == q:
                toggleIndex = left
            if reverseIndex == -1 and p != q:
                reverseIndex = left
            left += 1
        if left * 2 == B:
            break
    for i in range(B):
        if toggle:
            result[i] = 1 - result[i]
    if reverse:
        for i in range(B // 2):
            result[i], result[B - i - 1] = result[B - i - 1], result[i]
    print(''.join(map(str, result)))
    _ = input()
