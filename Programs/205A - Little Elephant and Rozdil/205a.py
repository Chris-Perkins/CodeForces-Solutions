# Description of the problem can be found at http://codeforces.com/problemset/problem/205/A

n = int(input())
l_n = list(map(int, input().split()))
m = min(l_n)
print("Still Rozdil" if l_n.count(m) > 1 else (l_n.index(m) + 1))