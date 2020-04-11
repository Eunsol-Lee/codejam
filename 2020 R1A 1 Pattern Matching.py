T = int(input())

for t in range(1, T + 1):
    N = int(input())
    left = []
    right = []
    leftMax = 0
    rightMax = 0
    result = ''
    possible = True
    for i in range(N):
        inputString = input()
        lFind = inputString.find('*')
        rFind = inputString.rfind('*')
        left.append(inputString[:lFind])
        right.append(inputString[rFind + 1:])
        if len(left[leftMax]) < len(left[-1]):
            leftMax = i
        if len(right[rightMax]) < len(right[-1]):
            rightMax = i
        result += inputString[lFind + 1:rFind].replace('*', '')

    for i in range(N):
        if left[i] != '' and left[i] != left[leftMax][:len(left[i])]:
            possible = False
        if right[i] != '' and right[i] != right[rightMax][-len(right[i]):]:
            possible = False
    if not possible:
        result = '*'
    else:
        result = left[leftMax] + result + right[rightMax]
    print('Case #{}: {}'.format(t, result))
