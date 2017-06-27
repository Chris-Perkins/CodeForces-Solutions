# Description of the problem can be found at 

from sys import stdin,stdout
input = stdin.readline

a, b = map(int, input().split())
n = list(input())
k = 0
for i in range(a - 1):
    if(n[i] == '.' and n[i + 1] == '.'):
        k += 1

while(b > 0):
    b -= 1
    x = input().split()
    i, l = int(x[0]), x[1]
    j = n[i - 1]
    n[i - 1] = l
    if(j == '.' and l != '.'):
        if(i !=1 and n[i-2] == '.'):
            k -= 1
        if(i != a and n[i] == '.'):
            k -= 1
    elif(j != '.' and l == '.'):
        if(i != 1 and n[i - 2] == '.'):
            k += 1
        if(i !=a and n[i] == '.'):
            k += 1
    stdout.write(str(k) + "\n")