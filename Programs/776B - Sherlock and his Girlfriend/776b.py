# Description of the problem can be found at http://codeforces.com/problemset/problem/776/B

import math


# returns a list of all prime numbers <= limit
# limit must be a positive number.
def sieve_of_eratosthenes(limit):
    # 0, 1 are not prime
    is_prime_array = [False] * 2 + [True] * (limit - 1)

    for num in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_array[num]:
            # go through every multiple of num (excluding num itself) and make it not prime
            is_prime_array[num * 2::num] = [False] * len(is_prime_array[num * 2::num])

    return set(num for num in range(len(is_prime_array)) if is_prime_array[num])

n = int(input())

s_p = sieve_of_eratosthenes(n + 2)


print(1 if n <= 2 else 2)
for i in range(2, n + 2):
    if i in s_p:
        print("1", end = " ")
    else:
        print("2", end = " ")
