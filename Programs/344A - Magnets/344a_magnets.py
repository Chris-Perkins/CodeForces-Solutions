# Description of the problem can be found at http://codeforces.com/problemset/problem/344/A

num_magnets = int(input())

# set previous string to something not seen before
prev_string = ""
num_groups = 0

for _ in range(num_magnets):
    magnet_in = input()
    
    if magnet_in != prev_string:
        num_groups += 1
        
    prev_string = magnet_in

print(num_groups)