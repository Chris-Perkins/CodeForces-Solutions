# Description of the problem can be found at http://codeforces.com/problemset/problem/25/A

# we do not need the first input, second input has our list of numbers
_, numbers = input(), list(map(int, input().split()))
num_evens = 0
num_odds = 0

index_even = 0
index_odd = 0

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        num_evens += 1
        index_even = index
    else:
        num_odds += 1
        index_odd = index
    
    if num_evens >= 2 and num_odds == 1:
        print(index_odd + 1)
        quit()
    elif num_odds >= 2 and num_evens == 1:
        print(index_even + 1)
        quit()