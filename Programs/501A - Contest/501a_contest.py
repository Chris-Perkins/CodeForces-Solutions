# Description of the problem can be found at http://codeforces.com/problemset/problem/501/A

a, b, c, d = map(int, input().split())
p_m = max(3 / 10 * a, a - (a / 250) * c)
p_v = max(3 / 10 * b, b - (b / 250) * d)

if p_m > p_v:
    print("Misha")
elif p_m < p_v:
    print("Vasya")
else:
    print("Tie")