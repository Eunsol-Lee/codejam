T = int(input())

for t in range(1, T + 1):
  N = int(input())
  F = [0] + list(map(int, input().split()))
  P = [0] + list(map(int, input().split()))
  u = [0] * (N + 1)
  queue = []
  incoming = [0] * (N + 1)
  final = 0

  for i in range(1, N + 1):
    incoming[P[i]] += 1
  for i in range(1, N + 1):
    if incoming[i] == 0:
      queue.append(i)

  while incoming[0]:
    now = queue.pop()
    target = P[now]

    incoming[target] -= 1

    if incoming[target] == 0:
      if u[target] == 0:
        F[target] = max(F[now], F[target])
      else:
        final += max(u[target], F[now])
        u[target] = min(u[target], F[now])
        F[target] = max(F[target], u[target])
      queue.append(target)
    else:
      if u[target] == 0:
        u[target] = F[now]
      else:
        final += max(u[target], F[now])
        u[target] = min(u[target], F[now])
  final += F[0]
  print(f'Case #{t}: {final}')

