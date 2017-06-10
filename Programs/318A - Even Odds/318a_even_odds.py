# Description of the problem can be found at http://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

# determine whether this is an even or odd number
even = True if k > n // 2 + n % 2 else False
if even:
    # subtract the number of odd numbers in our segment from current index
    print(2*(k - n // 2 - n % 2))
else:
    print(2*k - 1)