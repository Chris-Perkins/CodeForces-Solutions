# Description of the problem can be found at http://codeforces.com/problemset/problem/548/A

def is_pal(s, l, h):
    while l < h:
        if s[l] != s[h]:
            return False
        l += 1
        h -= 1
    
    return True

s = input()
k = int(input())
l = 0
h = len(s) // k - 1

if len(s) % k != 0:
    print("NO")
    quit()

while h < len(s):
    if not is_pal(s, l, h):
        print("NO")
        quit()
    
    l = h + 1
    h += len(s) // k

print("YES")