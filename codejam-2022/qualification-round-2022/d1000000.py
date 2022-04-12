T = int(input())

for t in range(1, T + 1):
  N = int(input())
  S = list(map(int, input().split()))
  S.sort()
  c = 0
  for i in range(1, len(S) + 1):
    if (c >= S[i - 1]):
      continue
    else: 
      c = c + 1
  print(f'Case #{t}: {c}')


