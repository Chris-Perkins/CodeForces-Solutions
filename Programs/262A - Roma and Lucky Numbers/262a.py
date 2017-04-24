# Description of the problem can be found at http://codeforces.com/problemset/problem/262/A

n, k = map(int, input().split())

t = 0
for x in input().split():
    t += 1 if (x.count("4") + x.count("7") <= k) else 0
print(t)