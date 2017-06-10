# Description of the problem can be found at http://codeforces.com/problemset/problem/602/A

def calc():
    n, b = map(int, input().split())
    x  =list(map(int, input().split()))
    a = 0
    for i in x:
        a = a * b + i
    return a

l_n = list()

for _ in range(2):
    l_n.append(calc())

if l_n[0] < l_n[1]:
    print("<")
elif l_n[1] < l_n[0]:
    print(">")
else:
    print("=")