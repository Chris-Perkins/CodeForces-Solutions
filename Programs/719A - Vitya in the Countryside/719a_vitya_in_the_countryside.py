# Description of the problem can be found at http://codeforces.com/problemset/problem/719/A

n = int(input())
l_m = list(map(int, input().split()))

if len(l_m) == 1 and l_m[n - 1] != 0 and l_m[n - 1] != 15:
    print("-1")
else:
    if l_m[n - 1] == 0:
        print("UP")
    elif l_m[n - 1] == 15:
        print("DOWN")
    elif l_m[n - 1] > l_m[n - 2]:
        print("UP")
    else:
        print("DOWN")