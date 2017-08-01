# Description of the problem can be found at http://codeforces.com/problemset/problem/835/A

s, v1, v2, t1, t2 = map(int, input().split())

print("First" if s * v1 + 2* t1 < s * v2 + 2 * t2 else ("Second" if s * v1 + 2 * t1 != s * v2 + 2 * t2 else "Friendship"))