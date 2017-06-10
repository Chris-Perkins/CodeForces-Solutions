# Description of the problem can be found at http://codeforces.com/contest/771/problem/B

n, k = map(int, input().split())
l_o = input().split()

a_n = ["A"]
for i in range(1, n):
    diff = i - 25 if i >= 25 else 0 
    a_n += [chr(ord("A") + i - (26 if diff != 0 else 0)) + ("" if diff == 0 else chr(ord("a") + diff))]

for i in range(n - k + 1):
    if l_o[i] == "NO":
        a_n[i + k - 1] = a_n[i]
print(" ".join(a_n))