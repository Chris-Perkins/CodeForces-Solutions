# Description of the problem can be found at http://codeforces.com/problemset/problem/811/A

a, b = map(int, input().split())

for i in range(1, int(1e9 + 1)):
    if i % 2 == 0:
        if i > b:
            print("Valera")
            quit()
        else:
            b -= i
    else:
        if i > a:
            print("Vladik")
            quit()
        else:
            a -= i