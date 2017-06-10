# Description of the problem can be found at http://codeforces.com/problemset/problem/535/A

n = int(input())

s = ""

if n == 0:
    s = "zero"
elif n // 10 == 1:
    if n % 10 == 0:
        s = "ten"
    elif n % 10 == 1:
        s = "eleven"
    elif n % 10 == 2:
        s = "twelve"
    elif n % 10 == 3:
        s = "thirteen"
    elif n % 10 == 4:
        s = "fourteen"
    elif n % 10 == 5:
        s = "fifteen"
    elif n % 10 == 6:
        s = "sixteen"
    elif n % 10 == 7:
        s = "seventeen"
    elif n % 10 == 8:
        s = "eighteen"
    elif n % 10 == 9:
        s = "nineteen"
    print(s)
    quit()
elif n // 10 > 1:
    if n // 10 == 9:
        s = "ninety"
    elif n // 10 == 8:
        s = "eighty"
    elif n // 10 == 7:
        s = "seventy"
    elif n // 10 == 6:
        s = "sixty"
    elif n // 10 == 5:
        s = "fifty"
    elif n // 10 == 4:
        s = "forty"
    elif n // 10 == 3:
        s = "thirty"
    elif n // 10 == 2:
        s = "twenty"
if n % 10 != 0:
    if n % 10 == 9:
        s = s + ("-" if len(s) > 0 else "") + "nine"
    elif n % 10 == 8:
        s = s + ("-" if len(s) > 0 else "") + "eight"
    elif n % 10 == 7:
        s = s + ("-" if len(s) > 0 else "") + "seven"
    elif n % 10 == 6:
        s = s + ("-" if len(s) > 0 else "") + "six"
    elif n % 10 == 5:
        s = s + ("-" if len(s) > 0 else "") + "five"
    elif n % 10 == 4:
        s = s + ("-" if len(s) > 0 else "") + "four"
    elif n % 10 == 3:
        s = s + ("-" if len(s) > 0 else "") + "three"
    elif n % 10 == 2:
        s = s + ("-" if len(s) > 0 else "") + "two"
    elif n % 10 == 1:
        s = s + ("-" if len(s) > 0 else "") + "one"
        
print(s)