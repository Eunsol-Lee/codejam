T = int(input())
for t in range(1, T + 1):
  R, C = map(int, input().split())
  print(f'Case #{t}:')
  print('..+' + '-+' * (C - 1))
  print('..|' + '.|' * (C - 1))
  print('+' + '-+' * C)
  for r in range(R - 1):
    print('|' + '.|' * C)
    print('+' + '-+' * C)