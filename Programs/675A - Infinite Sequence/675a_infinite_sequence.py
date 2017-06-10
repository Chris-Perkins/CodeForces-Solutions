# Description of the problem can be found at http://codeforces.com/problemset/problem/675/A

a, b, c = map(int, input().split())

if c == 0:
    if a == b:
        print("YES")
    else:
        print("NO")
elif (b - a) % c == 0 and (b - a) // c >= 0:
    print("YES")
else:
    print("NO")