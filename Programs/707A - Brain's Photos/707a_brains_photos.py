# Description of the problem can be found at http://codeforces.com/problemset/problem/707/A

r, c = map(int, input().split())

for _ in range(r):
    l = input().split()
    
    for t in l:
        if t != 'W' and t != 'B' and t != 'G':
            print("#Color")
            quit()
print("#Black&White")
