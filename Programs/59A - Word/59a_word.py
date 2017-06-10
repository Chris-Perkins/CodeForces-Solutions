# Description of the problem can be found at http://codeforces.com/problemset/problem/59/A

in_str = input()

num_lower = 0
num_upper = 0

for character in in_str:
    if character == character.upper():
        num_upper += 1
    else:
        num_lower += 1
    
print(in_str.upper() if num_upper > num_lower else in_str.lower())