# Description of the problem can be found at http://codeforces.com/problemset/problem/679/A

import sys

resp = list()

num = [2,3,5,7,4,9,25,49,11,13,17,19,23,29,31,37,41,43,47,53]

for i in num:
    print(i)
    sys.stdout.flush()
    resp.append(input())
if resp.count("yes") <= 1:
    print("prime")
    sys.stdout.flush()
else:
    print("composite")
    sys.stdout.flush()