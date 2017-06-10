# Description of the problem can be found at http://codeforces.com/problemset/problem/69/A


times = int(input())

# current forces
total_x, total_y, total_z = 0, 0, 0

for _ in range(times):
    this_x, this_y, this_z = map(int, input().split())
    total_x += this_x
    total_y += this_y
    total_z += this_z

if total_x == total_y == total_z == 0:
    print("YES")
else:
    print("NO")