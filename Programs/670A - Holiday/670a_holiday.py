# Description of the problem can be found at http://codeforces.com/problemset/problem/670/A

n = int(input())

print(str((n // 7) * 2 + (1 if n % 7 == 6 else 0)) + " " + str(((n + 5) // 7) * 2 + (1 if (n + 5) % 7 == 6 else 0)))