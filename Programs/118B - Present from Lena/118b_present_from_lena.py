# Description of the problem can be found at http://codeforces.com/problemset/problem/118/B

n = int(input())

r_c = 1
r_r = 1

c_n = -n

for i in range(n * 2 + 1):
    c_n_r = c_n
    r_c = 1
    
    for j in range(n * 2 + 1):
        if c_n_r >= 0:
            print(c_n_r, end = "" if (r_c == -1 and c_n_r == 0) else " ")
        else:
            if r_c == 1:
                print(" ", end = " ")
            else:
                break 
        
        c_n_r += r_c
        
        if j == n - 1:
            r_c = -1
    
    if i == n:
        r_r = -1
    
    c_n += r_r
        
    print()