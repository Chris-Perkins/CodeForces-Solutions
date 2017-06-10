# Description of the problem can be found at http://codeforces.com/problemset/problem/61/A

str1, str2 = input(), input()

for index in range(len(str1)):
    print(0 if str1[index] == str2[index] else 1, end="")