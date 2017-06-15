# Description of the problem can be found at http://codeforces.com/problemset/problem/584/B

n = int(input())

print((3**(3*n) - 7**n) % (int(1e9) + 7))