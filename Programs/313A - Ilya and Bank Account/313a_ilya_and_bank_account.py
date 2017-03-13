# Description of the problem can be found at http://codeforces.com/problemset/problem/313/A

bank_bal = input()
len_bal = len(bank_bal)

print(max(int(bank_bal), int(bank_bal[:len_bal - 2] + bank_bal[len_bal - 1]), int(bank_bal[:len_bal - 1])))