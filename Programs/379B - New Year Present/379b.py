# Description of the problem can be found at http://codeforces.com/problemset/problem/379/B

n = int(input())
l_n = list(map(int, input().split()))

s = ""
for i in range(n):
    if l_n[i] == 0:
        if i + 1 == n:
            print("".join(c for c in s))
            quit()
        else:
            s += "R"
    else:
        if i + 1 == n:
            s += "PLR" * (l_n[i] - 1) + "P"
        else:         
            s += "PRPL" * (min(l_n[i], l_n[i + 1])) + "PRL" * max(0, l_n[i] - l_n[i + 1] - 1) + ("PR" if (l_n[i] > l_n[i + 1]) else "R")
            l_n[i + 1] = max(l_n[i + 1] - l_n[i], 0)
            
print(s)