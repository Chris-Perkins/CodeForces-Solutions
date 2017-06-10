# Description of the problem can be found at http://codeforces.com/problemset/problem/697/A

t, s, x = map(int, input().split())

if t == x:
    print("YES")
else:
    if (x - t) % s <= 1 and (x - t) // s > 0:
        print("YES")
    else:
        print("NO")