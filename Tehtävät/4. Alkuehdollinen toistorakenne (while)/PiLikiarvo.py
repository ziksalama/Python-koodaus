import random

N = int(input("Syötä pisteiden määrä: "))
kerrat = 0
n = 0
while kerrat < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    kerrat += 1
    if x**2 + y**2 < 1:
        n += 1
pii = 4 * n / N
print(pii)