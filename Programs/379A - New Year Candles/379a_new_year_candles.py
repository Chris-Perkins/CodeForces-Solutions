# Description of the problem can be found at http://codeforces.com/problemset/problem/379/A

a, b = map(int, input().split())

total_hours = a
candles_out = a

while candles_out >= b:
    candles_out += 1 - b
    total_hours += 1
    
print(total_hours)