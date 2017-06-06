# Description of the problem can be found at http://codeforces.com/problemset/problem/387/A

l_s = list(map(int, input().split(":")))
l_t = list(map(int, input().split(":")))

if l_t[1] > l_s[1]:
    l_s[0] -= 1
    
print("%02d:%02d" % ((l_s[0] - l_t[0]) % 24, (l_s[1] - l_t[1]) % 60))