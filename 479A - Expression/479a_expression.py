# Description of the problem can be found at http://codeforces.com/problemset/problem/479/A

a, b, c = int(input()), int(input()), int(input())
print(max(a+b+c, a*b*c, (a+b)*c, a*(b+c)))