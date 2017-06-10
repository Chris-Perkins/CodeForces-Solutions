# Description of the problem can be found at http://codeforces.com/problemset/problem/735/A

n, k = map(int, input().split())
s = input()
s_t = set(["G", "T"])

p = 0
for i in range(len(s)):
    if s[i] in s_t:
        p = i
        break
    
p += k
while p < len(s):
    if s[p] in s_t:
        print("YES")
        quit()
    elif s[p] == "#":
        print("NO")
        quit()
    p += k
print("NO")