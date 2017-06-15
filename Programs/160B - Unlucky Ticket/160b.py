# Description of the problem can be found at http://codeforces.com/problemset/problem/160/B

n = int(input())
s = input()

l_1 = list()
l_2 = list()

for c in s[:n]:
    l_1.append(int(c))
for c in s[n:]:
    l_2.append(int(c))

l_1.sort()
l_2.sort()

if(l_1[0] == l_2[0]):
    print("NO")
    quit()
else:
    g = l_1[0] > l_2[0]

for i in range(1, n):
    if g and l_1[i] > l_2[i]:
        pass
    elif not g and l_1[i] < l_2[i]:
        pass
    else:
        print("NO")
        quit()
print("YES")