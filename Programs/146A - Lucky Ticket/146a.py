# Description of the problem can be found at http://codeforces.com/problemset/problem/146/A

n = int(input())
s = input()

if len(s.replace("4", "").replace("7", "")) != 0:
    print("NO")
    quit()
if sum(int(x) for x in s[:len(s) // 2]) != sum(int(x) for x in s[len(s) // 2:]):
    print("NO")
    quit()
print("YES")