# Description of the problem can be found at http://codeforces.com/problemset/problem/810/A

n, k = map(int, input().split())
s = sum(map(int, input().split()))

print(max(0, n * k * 2 - n - s * 2))