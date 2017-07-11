# Description of the problem can be found at http://codeforces.com/problemset/problem/555/A

n, k = map(int, input().split())

a =  2 * n - k + 1

for _ in range(k):
    x = list(map(int, input().split()))[1:]
    for i in range(len(x)):
        if i + 1 == x[i]:
            a -= 2
            
print(a)