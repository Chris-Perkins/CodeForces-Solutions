# Description of the problem can be found at http://codeforces.com/problemset/problem/405/A

_ = input()

output_list = list(map(int, input().split()))
output_list.sort()

for num in output_list:
    print(num, end = " ")

