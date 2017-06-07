# Description of the problem can be found at http://codeforces.com/problemset/problem/716/B

def fill_in(s):
    s_a = set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    s_x = set(x for x in s)
    if "?" in s_x:
        s_x.remove("?")
    for x in s_x:
        s_a.remove(x)
    
    s_o = list()
    for x in s:
        if x == "?":
            s_o.append(s_a.pop())
        else:
            s_o.append(x)
    return "".join(s_o)

s = input()

d_c = {}

for i in range(len(s)):  
    if s[i] not in d_c:
        d_c[s[i]] = 0
    d_c[s[i]] += 1
    
    if i >= 25:
        if len(d_c) - (1 if "?" in d_c else 0) + (0 if "?" not in d_c else d_c["?"]) == 26:
            s_f = s[:i - 25].replace("?", "A")
            s_l = ("" if i + 1 == len(s) else s[i + 1:].replace("?", "A"))
            s = s_f + fill_in(s[i - 25: i + 1]) + s_l
            print(s)
            quit()
        d_c[s[i - 25]] -= 1
        if d_c[s[i - 25]] == 0:
            del d_c[s[i - 25]]
print(-1)