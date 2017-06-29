# Description of the problem can be found at http://codeforces.com/problemset/problem/724/A

d = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
l_n = list([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

x = input()
y = input()

for i in range(0, 11):
    if (l_n[i] + d[x]) % 7 == d[y]:
        print("YES")
        quit()
print("NO")