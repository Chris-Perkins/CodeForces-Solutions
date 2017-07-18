# Description of the problem can be found at http://codeforces.com/problemset/problem/675/B

n, a, b, c, d = map(int,input().split())
arr = [a + b, a + c, b + d, c + d]
count = n * (n - max(arr) + min(arr))
print(max(0, count))