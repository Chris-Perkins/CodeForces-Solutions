# Description of the problem can be found at http://codeforces.com/problemset/problem/740/A

n, c1, c2, c3 = map(int, input().split())


if n % 4 == 0:
    print(0)
elif n % 4 == 1:
    print(min([c3, c2 + c1, c1 * 3]))
elif n % 4 == 2:
    print(min([c2, c1 * 2, c3 * 2]))
else:
    print(min([c3 * 3, c2 + c3, c1]))