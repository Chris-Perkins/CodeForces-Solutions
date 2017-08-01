# Description of the problem can be found at http://codeforces.com/problemset/problem/805/D

sums = [0] * (10**6 + 1)


def exp_two_sum(num):
    if num != 0 and sums[num] == 0:
        sums[num] = 2**(num - 1) + exp_two_sum(num - 1)
    return sums[num]

s = input()
m = int(1e9) + 7

c_a = 0
t = 0
for c in s:
    if c == "a":
        c_a += 1
    else:
        t += exp_two_sum(c_a)

print(t % m)