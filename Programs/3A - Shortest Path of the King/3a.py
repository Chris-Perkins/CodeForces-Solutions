# Description of the problem can be found at http://codeforces.com/problemset/problem/3/A

p1 = list(input())
p2 = list(input())

l_m = list()

while p1[0] != p2[0] or p1[1] != p2[1]:
    s = ""
    
    if p1[0] < p2[0]:
        s = "R"
        p1[0] = chr(ord(p1[0]) + 1)
    elif p1[0] > p2[0]:
        s = "L"
        p1[0] = chr(ord(p1[0]) - 1)
        
    if p1[1] < p2[1]:
        s = s + "U"
        p1[1] = str(int(p1[1]) + 1)
    elif p1[1] > p2[1]:
        s = s + "D"
        p1[1] = str(int(p1[1]) - 1)
        
    l_m.append(s)

print(len(l_m))
print("\n".join(l_m))