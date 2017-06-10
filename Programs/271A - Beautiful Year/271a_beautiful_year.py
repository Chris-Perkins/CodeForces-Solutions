# Description of the problem can be found at http://codeforces.com/problemset/problem/271/A

in_num = int(input()) + 1

while len(set(str(in_num))) < 4:
	in_num += 1

print(in_num)