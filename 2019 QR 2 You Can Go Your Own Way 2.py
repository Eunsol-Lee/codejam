T = int(input())
for t in range(T):
    N = int(input())
    P = input()
    print('Case #{}: {}'.format(
        t + 1, P.replace('S', 'F').replace('E', 'S').replace('F', 'E')))
