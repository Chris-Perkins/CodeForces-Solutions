# Description of the problem can be found at http://codeforces.com/problemset/problem/535/B

n = input()

i = 1
for c in n:
    i *= 2
    i += 1 if c == "7" else 0

print(i - 1) 