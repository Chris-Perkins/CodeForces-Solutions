# Description of the problem can be found at http://codeforces.com/problemset/problem/518/A

s, t = input(), input()
for i in range(len(s)):
    if s[i] == 'z':
        continue
    c = chr(ord(s[i]) + 1)
    st = s[0:i] + c + ('a' * (len(s) - i - 1));
    if st < t:
        print(st)
        exit()
print("No such string")