n, m = map(int, input().split(), )

while (m > 0):
    n = int(n / 10) if n % 10 == 0 else (n - 1)
    m -= 1

print(n)