# Description of the problem can be found at http://codeforces.com/problemset/problem/404/A

n = int(input())

l = 0
d = None
o = None
for i in range(n):
    s = input()
    for i in range(len(s)):
        if not d:
            d = s[i]
        elif not o:
            o = s[i]
            if o == d:
                print("NO")
                quit()
        elif l == i or n - l - 1 == i:
            if s[i] != d or s[n - l - 1] != d:
                print("NO")
                quit()
        else:
            if s[i] != o:
                print("NO")
                quit()
    l += 1
print("YES")