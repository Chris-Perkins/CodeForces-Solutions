# Description of the problem can be found at http://codeforces.com/problemset/problem/659/A

n, a, b = map(int, input().split())
b %= n

print(((a + b) % n) if (a + b) % n != 0 else n)