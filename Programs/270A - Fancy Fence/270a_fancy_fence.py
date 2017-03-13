# Description of the problem can be found at http://codeforces.com/problemset/problem/270/A

for i in range(int(input())):
    print("YES" if 360 % (180 - int(input())) == 0 else "NO")