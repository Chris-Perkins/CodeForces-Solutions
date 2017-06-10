# Description of the problem can be found at http://codeforces.com/contest/782/problem/D
# If you would like to learn about my approach to this problem from myself, please feel free
# to contact me and I'll be happy to guide you through this recursion :)

d = {}
l_s = None
f_l = None

# attempts to add s into our list of names as specified in problem specs
def add_if_poss(s, i):
    if s == None:
        print("NO")
        quit()
    elif s not in d:
        d[s] = i
        f_l[i] = s
    else:
        if d[s] != -1:
            # if we can't swap, try to change our string
            if l_s[d[s]] == None:
                t_s = l_s[i]
                l_s[i] = None
                add_if_poss(t_s, i)
                f_l[i] = t_s
            # if we can swap, we have to change the stored string to second variation
            else:
                t_i = d[s]
                t_s = l_s[d[s]]
                l_s[d[s]] = None
                d[s] = -1
                add_if_poss(t_s, t_i)
                add_if_poss(s, i)
        elif d[s] == -1:
			# if this place is taken inherently and we're adding a "second" name
            if l_s[i] == None:
                d[s] = i
                f_l[i] = s
			# if we're adding a "first" name, try to add a "second" name
            else:
                t_s = l_s[i]
                l_s[i] = None
                add_if_poss(t_s, i)


n = int(input())
l_s = [""]*n
f_l = [""]*n

for i in range(n):
    s = input().split()
    s0 = s[0][:3]
    s1 = s[0][:2] + s[1][0]
    l_s[i] = s1
    
    add_if_poss(s0, i)

print("YES")
print("\n".join(f_l))