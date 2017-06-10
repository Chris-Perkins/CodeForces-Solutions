# Description of the problem can be found at http://codeforces.com/problemset/problem/617/B

t = int(input())
l_n = list(input().split())

p_1 = None
t = 1
for i in range(len(l_n)):
    if l_n[i] == "1":
        if p_1 == None:
            p_1 = i
        else:
            t *= (i - p_1)
            p_1 = i
print(t if p_1 != None else 0)