# Description of the problem can be found at http://codeforces.com/problemset/problem/798/A

def isPal(s, i):
    j = 0
    
    while j < len(s) // 2 + (1 if len(s) % 2 == 1 else 0):
        if j != i:
            if s[j] != s[len(s) - 1 - j]:
                return False
        j += 1
    return True

s = input()

if len(s) % 2 != 1 and isPal(s, -1):
    print("NO")
    quit()

i = 0
while i < len(s) // 2 + (1 if len(s) % 2 == 1 else 0):
    if isPal(s, i):
        print("YES")
        quit()
    i += 1
    
print("NO")