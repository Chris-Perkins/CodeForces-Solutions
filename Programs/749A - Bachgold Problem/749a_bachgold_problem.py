# Description of the problem can be found at http://codeforces.com/problemset/problem/749/A

n = int(input())
n_t = 0

while n > 3:
    n -= 2
    n_t += 1

if n == 3:
    print(str(n_t + 1) + "\n3", end = " ")
    for _ in range(n_t):
        print("2", end = " ")
else:
    print(n_t + 1)
    for _ in range(n_t + 1):
        print("2", end = " ")