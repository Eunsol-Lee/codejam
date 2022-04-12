T = int(input())

for t in range(1, T + 1):
  N = int(input())
  L = list(map(int, input().split()))
  count = 0
  for i in range(N - 1):
    m = min(L[i:])
    position = L[i:].index(m) + i
    for j in range(i, i + int((position - i + 1) / 2)):
      temp = L[j]
      L[j] = L[position - j + i]
      L[position - j + i] = temp
    count += position - i + 1
  print(f'Case #{t}: {count}')