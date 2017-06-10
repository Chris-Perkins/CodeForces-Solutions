# Description of the problem can be found at http://codeforces.com/problemset/problem/445/A

n, m = map(int, input().split())

for i in range(n):
    l_b = input()
    for j in range(m):
        print("-" if l_b[j] == "-" else ("B" if (i + j) % 2 == 0 else "W"), end = "")
    print()