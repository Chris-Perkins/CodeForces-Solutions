# Description of the problem can be found at http://codeforces.com/problemset/problem/109/A

n = int(input())

for i in range(n // 7 + 1):
    for j in range((n - 7 * (n // 7 - i)) // 4 + 1):
        if (n // 7 - i) * 7 + j * 4 == n:
            print("4" * j + "7" * (n // 7 - i))
            quit()
        elif (n // 7 - i) * 7 + j * 4 > n:
            break
print(-1)