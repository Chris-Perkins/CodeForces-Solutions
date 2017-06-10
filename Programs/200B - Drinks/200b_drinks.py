# Description of the problem can be found at http://codeforces.com/problemset/problem/200/B

n = int(input())
print(sum(int(x) for x in input().split()) / n)