# Description of the problem can be found at http://codeforces.com/problemset/problem/433/A

n = int(input())

l_w = list(map(int, input().split()))

n200 = 0
n100 = 0

for w in l_w:
    if w == 200:
        n200 += 1
    else:
        n100 += 1

for i in range(n200 + 1):
    for j in range(n100 + 1):
        if i * 200 + j * 100 == (n200 - i) * 200 + (n100 - j) * 100:
            print("YES")
            quit()
print("NO")