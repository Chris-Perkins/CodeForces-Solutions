# Description of the problem can be found at http://codeforces.com/problemset/problem/492/A

last_num = 0
last_sum = 0

num_cubes = int(input())

while num_cubes >= 0:
    last_num += 1
    last_sum += last_num
    num_cubes -= last_sum

print(last_num - 1)