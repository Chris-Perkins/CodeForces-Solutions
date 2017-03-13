# Description of the problem can be found at http://codeforces.com/problemset/problem/41/A

s, t = input(), input()

# This case isn't mentioned by the problem, but I don't want to be wrong.
if (len(s) != len(t)):
    print("NO")
    quit()

for index in range(len(s)):
    if s[index] != t[len(s) - index - 1]:
        print("NO")
        quit()
        
print("YES")