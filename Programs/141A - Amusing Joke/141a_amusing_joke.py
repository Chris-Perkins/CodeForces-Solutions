# Description of the problem can be found at http://codeforces.com/problemset/problem/141/A

names = input() + input()
scrambled = input()

names = "".join(sorted(names))
scrambled = "".join(sorted(scrambled))

print("YES" if names == scrambled else "NO")