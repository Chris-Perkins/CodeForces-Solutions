# Description of the problem can be found at http://codeforces.com/contest/777/problem/0

num_moves = int(input()) % 6
found_position = int(input())

while num_moves > 0:
    if num_moves % 2 == 0:
        if found_position == 2:
            found_position = 1
        elif found_position == 1:
            found_position = 2
    else:
        if found_position == 1:
            found_position = 0
        elif found_position == 0:
            found_position = 1
    
    num_moves -= 1
    
print (found_position)