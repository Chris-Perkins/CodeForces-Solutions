# Description of the problem can be found at http://codeforces.com/problemset/problem/579/A

def get_one_bits(n):
    if n == 0:
        return 0
    return n % 2 + get_one_bits(n // 2)

n = int(input())
print(get_one_bits(n))