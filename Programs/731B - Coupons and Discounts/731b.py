# Description of the problem can be found at http://codeforces.com/problemset/problem/731/B

n = int(input())

l_p = list(map(int, input().split()))

for i in range(len(l_p)):
    if l_p[i] % 2 == 1:
        if i + 1 == len(l_p) or l_p[i + 1] == 0:
            print("NO")
            quit()
        l_p[i + 1] -= 1
print("YES")