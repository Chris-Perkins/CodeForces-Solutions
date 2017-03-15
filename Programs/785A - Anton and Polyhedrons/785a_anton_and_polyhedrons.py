# Description of the problem can be found at http://codeforces.com/contest/785/problem/0

d = {}
d["T"] = 4
d["C"] = 6
d["O"] = 8
d["D"] = 12
d["I"] = 20

t = 0

for _ in range(int(input())):
	t+= d[input()[0]]
	
print(t)