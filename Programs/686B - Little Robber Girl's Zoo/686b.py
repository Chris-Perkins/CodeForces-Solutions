# Description of the problem can be found at http://codeforces.com/problemset/problem/686/B

n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(j + 1, j + 2)