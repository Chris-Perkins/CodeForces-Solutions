# Description of the problem can be found at http://codeforces.com/problemset/problem/747/A

import math

n = int(input())

for i in range(1, int(math.sqrt(n)) + 1)[::-1]:
    if n % i == 0:
        print(" ".join([str(i), str(n // i)]))
        quit()