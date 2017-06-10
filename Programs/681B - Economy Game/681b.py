# Description of the problem can be found at http://codeforces.com/problemset/problem/681/B

n = int(input())

for i in range(0, n // 1234567 + 1):
    for j in range(0, (n - i * 1234567) // 123456 + 1):
        if ((n - i * 1234567) - j * 123456) % 1234 == 0:
            print("YES")
            quit()
print("NO")