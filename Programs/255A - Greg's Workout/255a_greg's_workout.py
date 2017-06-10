# Description of the problem can be found at http://codeforces.com/problemset/problem/255/A

n = int(input())

l_n = list(map(int, input().split()))
a_t = [0]*3

for i in range(n):
    a_t[i % 3] += l_n[i]

if a_t[0] > a_t[1] and a_t[0] > a_t[2]:
    print("chest")
elif a_t[1] > a_t[2]:
    print("biceps")
else:
    print("back")