T = int(input())
for t in range(1, T + 1):
    N = int(input())
    task = []
    for i in range(N):
        task.append(tuple(map(int, (input() + ' ' + str(i)).split())))
    task = sorted(task)
    c1 = 0
    c2 = 0
    result = ''
    for i in range(N):
        if task[i][0] >= c1:
            c1 = task[i][1]
            result += 'J'
        else:
            if task[i][0] >= c2:
                c2 = task[i][1]
                result += 'C'
            else:
                result = 'IMPOSSIBLE'
                break
    if result != 'IMPOSSIBLE':
        newResult = ''
        for i in range(N):
            for j in range(N):
                if task[j][2] == i:
                    newResult += result[j]
    else:
        newResult = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t, newResult))
