# Description of the problem can be found at http://codeforces.com/problemset/problem/766/B

n = int(input())
l_n = list(map(int, input().split()))
l_n.sort()

for i in range(1, n - 1):
    if (l_n[i - 1] + l_n[i] > l_n[i + 1]):
        print("YES")
        quit()
print("NO")