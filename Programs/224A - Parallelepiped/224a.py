# Description of the problem can be found at http://codeforces.com/problemset/problem/224/A

import math

v1, v2, v3 = map(int, input().split())

print(int(4*(math.sqrt(v1*v2 / v3) + math.sqrt(v2*v3 / v1) + math.sqrt(v1*v3 / v2))))