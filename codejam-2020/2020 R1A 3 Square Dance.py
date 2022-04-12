T = int(input())

for t in range(1, T + 1):
    R, C = map(int, input().split())
    for i in range(R):
        cells = list(map(int, input().split()))
