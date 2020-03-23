T = int(input())

for t in range(T):
    N = int(input())
    A = 0
    B = 0
    C = 1
    while N:
        p = N % 10
        if p == 4:
            A += C * 3
            B += C * 1
        else:
            A += C * p
        C *= 10
        N //= 10
    print('Case #{}: {} {}'.format(t + 1, A, B))
