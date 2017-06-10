# Description of the problem can be found at http://codeforces.com/problemset/problem/514/A

n = input()

for i in range(len(n)):
    if i == 0:
        if (9 - int(n[i]) < int(n[i]) and 9 - int(n[i]) != 0) or n[i] == "0":
            print(9 - int(n[i]), end = "")
        else:
            print(n[i], end = "")
    else:
        if 9 - int(n[i]) < int(n[i]):
            print(9 - int(n[i]), end = "")
        else:
            print(n[i], end = "")