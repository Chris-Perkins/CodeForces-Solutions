# Description of the problem can be found at http://codeforces.com/problemset/problem/258/A

n = input()

for i in range(len(n)):
    if n[i] == "0":
        print(n[:i] + n[i + 1:])
        quit()
print(n[:len(n) - 1])