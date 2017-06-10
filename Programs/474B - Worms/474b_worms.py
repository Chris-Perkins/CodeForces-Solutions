# Description of the problem can be found at http://codeforces.com/problemset/problem/474/B

n = int(input())
b = []
b.append(0)
l_n = list(map(int, input().split()))

for i in range(len(l_n)):
    for _ in range(l_n[i]):
        b.append(i + 1)

_ = input()
for v in list(map(int, input().split())):
    print(b[v])