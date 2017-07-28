# Description of the problem can be found at http://codeforces.com/problemset/problem/801/A

s = input()
count = s.count('VK')
if "VV" in s.replace("VK", "-") or "KK" in s.replace("VK", "-"):
    count += 1
print(count)