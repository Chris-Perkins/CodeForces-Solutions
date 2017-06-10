# Description of the problem can be found at http://codeforces.com/problemset/problem/488/A

a = int(input())
b = 1

a += 1
while ("8" not in str(a)):
    a += 1
    b += 1
    
print(b)