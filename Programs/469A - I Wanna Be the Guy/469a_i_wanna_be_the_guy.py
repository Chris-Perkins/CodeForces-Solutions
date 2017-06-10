# Description of the problem can be found at http://codeforces.com/problemset/problem/469/A

num_levels = int(input())

seen = set()

# go through 2 lines for each person that wants to be the guy
for _ in range(2):
    levels = list(map(int, input().split()))
    levels = levels[1:]
    seen.update(levels)
    
for i in range(num_levels):
    # see if we can complete this level
    if not (i + 1) in seen:
        print("Oh, my keyboard!")
        quit()

print("I become the guy.")