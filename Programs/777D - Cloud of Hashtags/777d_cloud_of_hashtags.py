# Description of the problem can be found at http://codeforces.com/problemset/problem/777/D

num = int(input())
hts = list(input() for _ in range(num))

i = num - 2
while i >= 0:
    if hts[i] > hts[i + 1]:
        n = 1
        while n < len(hts[i + 1]) and hts[i][n] == hts[i + 1][n]: 
            n += 1
        hts[i] = hts[i][:n]
    i -= 1
    
print("\n".join(hts))