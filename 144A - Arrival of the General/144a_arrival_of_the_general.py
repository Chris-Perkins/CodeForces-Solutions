# Description of the problem can be found at http://codeforces.com/problemset/problem/144/A

_ = input()
soldiers = list(map(int, input().split()))

# holds height of our soldiers
min_height = None
min_index = None

# holds max height of our soldiers
max_height = None
max_index = None

for index in range(len(soldiers)):
    # start out by removing all none types
    if min_height == None:
        min_height = max_height = soldiers[index]
        min_index = max_index = index
    # since we parse through, we want to find the lowest guy
    # that appears last. So if we have 3 3 3 4 as input, we
    # want to move the last "3" to the lowest position.
    elif soldiers[index] <= min_height:
        min_height = soldiers[index]
        min_index = index
    # the same but opposite logic is applied to max height.
    elif soldiers[index] > max_height:
        max_height = soldiers[index]
        max_index = index

# What a print statement.
# We want to print the number of shifts necessary to move the largest guy to the front
# which is equivalent to the max index,
# then we want to add the result of the total soldiers [0 indexed] - the index of the shortest
# soldier to find how many shifts are necessary to shift the shortest soldier to the end.
# Finally, we subtract one if we end up shifting the shortest soldier and largest soldier
# in one move to account for overlap.
print(max_index + len(soldiers) - 1 - min_index - (1 if min_index < max_index else 0))
        
    