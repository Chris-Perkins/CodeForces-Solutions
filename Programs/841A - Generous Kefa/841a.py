# Description of the problem can be found at http://codeforces.com/problemset/problem/841/A

n, k = map(int, input().split())
dict_chars = {}
for c in input():
    if c not in dict_chars:
        dict_chars[c] = 0
    dict_chars[c] += 1
    if dict_chars[c] / k > 1:
        print("NO")
        quit()
print("YES")