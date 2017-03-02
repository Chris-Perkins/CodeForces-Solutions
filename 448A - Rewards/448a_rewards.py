# Description of the problem can be found at http://codeforces.com/problemset/problem/448/A

import math

a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
n = int(input())

if int(math.ceil(a / 5)) + int(math.ceil(b / 10)) <= n:
    print("YES")
else:
    print("NO")