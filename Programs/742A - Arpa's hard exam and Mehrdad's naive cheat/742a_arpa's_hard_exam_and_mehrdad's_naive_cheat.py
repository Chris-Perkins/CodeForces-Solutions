# Description of the problem can be found at http://codeforces.com/problemset/problem/742/A

n = int(input())

if n == 0:
    print("1")
elif (n - 1) % 4 == 0:
    print("8")
elif (n - 1) % 4 == 1:
    print("4")
elif (n - 1) % 4 == 2:
    print("2")
else:
    print("6")