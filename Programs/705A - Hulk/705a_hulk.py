# Description of the problem can be found at http://codeforces.com/problemset/problem/705/A

ans = ""
prev = False
n = int(input())

while n > 0:
    if prev:
        if n == 1:
            ans += "I love it"
        else:
            ans += "I love that "
    else:
        if n == 1:
            ans += "I hate it"
        else:
            ans+= "I hate that "
    n -= 1
    prev = not prev

print(ans)
        