# Description of the problem can be found at http://codeforces.com/problemset/problem/75/A

a = input()
b = input()

if (str(int(a.replace("0", "")) + int(b.replace("0", ""))) == (str(int(a) + int(b))).replace("0", "")):
    print("YES")
else:
    print("NO")