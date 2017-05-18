# Description of the problem can be found at http://codeforces.com/problemset/problem/779/A

n = int(input())

l_s1 = [0 for i in range(5)]
l_s2 = [0 for i in range(5)]
l_d = [0 for i in range(5)]

for i in list(map(int, input().split())):
    l_s1[i - 1] += 1
for i in list(map(int, input().split())):
    l_s2[i - 1] += 1

for i in range(5):
    l_d[i] = abs(l_s1[i] - l_s2[i])
    if l_d[i] % 2 == 1:
        print(-1)
        quit()
    else:
        l_d[i] //= 2

if sum(l_d) % 2 == 1:
    print(-1)
    quit()
else:
    print(sum(l_d) // 2)