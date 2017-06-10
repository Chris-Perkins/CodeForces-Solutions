# Description of the problem can be found at http://codeforces.com/problemset/problem/6/A

l_s = list(map(int, input().split()))
l_s.sort()

for i in range(0, 2):
    if sum(l_s[i: i + 2]) > l_s[i + 2]:
        print("TRIANGLE")
        quit()
        
for i in range(0, 2):
    if sum(l_s[i: i + 2]) == l_s[i + 2]:
        print("SEGMENT")
        quit()

print("IMPOSSIBLE")