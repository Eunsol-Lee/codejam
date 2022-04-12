T = int(input())
for t in range(1, T + 1):
  c1, m1, y1, k1 = map(int, input().split())
  c2, m2, y2, k2 = map(int, input().split())
  c3, m3, y3, k3 = map(int, input().split())
  cmin = min(c1, c2, c3)
  mmin = min(m1, m2, m3)
  ymin = min(y1, y2, y3)
  kmin = min(k1, k2, k3)
  if cmin + mmin + ymin + kmin < 1000000:
    print (f'Case #{t}: IMPOSSIBLE')
  else:
    cmin = min(cmin, 1000000)
    mmin = min(mmin, 1000000 - cmin)
    ymin = min(ymin, 1000000 - cmin - mmin)
    kmin = min(kmin, 1000000 - cmin - mmin - ymin)
    print(f'Case #{t}: {cmin} {mmin} {ymin} {kmin}')
