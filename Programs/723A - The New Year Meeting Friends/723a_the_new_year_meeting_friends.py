# Description of the problem can be found at http://codeforces.com/problemset/problem/723/A

l = list(map(int, input().split()))
l.sort()
print(l[2] - l[0])