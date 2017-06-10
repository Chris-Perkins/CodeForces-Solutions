# Description of the problem can be found at http://codeforces.com/problemset/problem/339/B

n, _ = map(int, input().split())
tasks = list(map(int, input().split()))

cur_house = 1
cur_time = 0

for task in tasks:
    cur_time += (task - cur_house) % n
    cur_house = task

print(cur_time)