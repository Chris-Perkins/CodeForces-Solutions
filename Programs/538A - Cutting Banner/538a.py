# Description of the problem can be found at http://codeforces.com/problemset/problem/538/A

s = input()

d = [c for c in "CODEFORCES"]

if len(s) < len("CODEFORCES"):
    print("NO")
    quit()

p = False
st = -1
e = -1
c_s = 0

for i in range(len(s)):
    if st == - 1 and (i >= len(d) or s[i] != d[i]):
        st = i
        break
    elif st == -1 and s[i] == d[i]:
        d[i] = "!"
        if i == len(s) - 1:
            print("YES")
            quit()


for i in range(len(s)):
    if e == -1 and (i >= len(d) or s[len(s) - 1 - i] != d[len(d) - 1 - i]):
        e = len(s) - 1 - i

    if e != -1 and st != -1:
        break

if s[:st] + s[e + 1:] == "CODEFORCES":
    print("YES")
    quit()
else:
    print("NO")
    quit()