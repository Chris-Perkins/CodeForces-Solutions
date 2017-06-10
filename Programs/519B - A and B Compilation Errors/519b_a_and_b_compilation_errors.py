# Description of the problem can be found at http://codeforces.com/problemset/problem/519/B

_ = input()
l1 = sum(map(int, input().split()))
l2 = sum(map(int, input().split()))
l3 = sum(map(int, input().split()))

print(l1 - l2)
print(l2 - l3)