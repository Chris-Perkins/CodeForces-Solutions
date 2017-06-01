# Description of the problem can be found at http://codeforces.com/problemset/problem/708/A

s = input()

c_i = None
c_i_e = len(s)
for i in range(len(s)):
    if s[i] != "a":
        if c_i == None:
            c_i = i
    elif c_i != None:
        c_i_e = i
        break

if c_i == None:
    print(s[0:len(s) - 1], end="")
    print("z")
else:   
    print(s[0:c_i], end="")
    for i in range(c_i, c_i_e):
        if s[i] == 'a':
            print('z', end = "")
        else:
            print(chr(ord(s[i]) - 1), end="")
    print(s[c_i_e:])