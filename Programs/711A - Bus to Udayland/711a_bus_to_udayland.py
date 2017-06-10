# Description of the problem can be found at http://codeforces.com/problemset/problem/711/A

n = int(input())
l = list()
found_ans = False

for _ in range(n):
    r = input()
    
    if not found_ans:
        if r[0] == r[1] == 'O':
            r = "++" + r[2:]
            found_ans = True
            
        elif r[3] == r[4] == 'O': 
            r = r[:3] + "++"
            found_ans = True
    
    l.append(r)

print("NO" if not found_ans else ("YES\n" + "\n".join(l)))