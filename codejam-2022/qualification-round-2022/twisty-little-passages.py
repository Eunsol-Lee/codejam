import random

T = int(input())

for t in range(1, T + 1):
  N, K = map(int, input().split())
  passages = [0] * N
  count = 0
  for k in range(0, K):
    R, P = map(int, input().split())
    passages[R - 1] = P

    if k % 2 == 0:  
      while 1:
        t = random.randint(1, N)
        if passages[t - 1] == 0:
          print(f'T {t}')
          break
    else:
      print('W')
    
  R, P = map(int, input().split())
  passages[R - 1] = P
  for k in range(N):
    count += passages[k]
  count = round(count / 2)
  print('E', count)
