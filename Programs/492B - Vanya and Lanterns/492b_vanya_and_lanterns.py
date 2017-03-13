# Description of the problem came from http://codeforces.com/problemset/problem/492/B

l_lanterns = list()

_, l = map(int, input().split())
l_lanterns.append(0)
l_lanterns.append(l)

s_lanterns = set(map(int, input().split()))

l_lanterns.extend(s_lanterns)
l_lanterns.sort()

max_dist = -1

for index in range(len(l_lanterns) - 1):
    num_lanterns = 1 if l_lanterns[index +1] in s_lanterns else 0
    num_lanterns += 1 if l_lanterns[index] in s_lanterns else 0
    max_dist = max(max_dist, (l_lanterns[index + 1] - l_lanterns[index]) / num_lanterns)

print(max_dist)