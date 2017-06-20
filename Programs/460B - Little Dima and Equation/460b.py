# Description of the problem can be found at http://codeforces.com/problemset/problem/460/B

a, b, c = map(int, input().split())

l_a = list()
for i in range(1, 82):
    x = b * (i ** a) + c
    
    if x >= 0 and x <= int(1e9) and sum(map(int, str(x))) == i:
        l_a.append(str(x))
        
print(len(l_a))
print(" ".join(l_a))