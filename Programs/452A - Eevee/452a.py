# Description of the problem can be found at http://codeforces.com/problemset/problem/452/A

l_n = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]

n = int(input())
s = input()

l_n = [x for x in l_n if len(x) == n]
for x in l_n:
    for i in range(len(s)):
        if s[i] != "." and s[i] != x[i]:
            break
        elif i + 1 == len(s):
            print(x)
            quit()