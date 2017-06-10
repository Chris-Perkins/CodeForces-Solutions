# Description of the problem can be found at http://codeforces.com/problemset/problem/732/C

l_t = list(map(int, input().split()))

print(sum(max(0, max(l_t) - x - 1) for x in l_t))