# Description of the problem can be found at http://codeforces.com/problemset/problem/550/A

s = input()

a = s.find("AB")
b = s[a + 2:].find("BA")
c = s.find("BA")
d = s[c + 2:].find("AB")

print("YES" if a >= 0 and b >= 0 or c >= 0 and d >= 0 else "NO")