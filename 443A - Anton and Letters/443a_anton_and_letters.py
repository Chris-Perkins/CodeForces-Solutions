# Description of the problem can be found at http://codeforces.com/problemset/problem/443/A

letters = input().split(", ")
# chop off the first bracket character
letters[0] = letters[0][1:]
# a very long way of saying "chop off the last character ('}') from the last string"
letters[len(letters) - 1] = letters[len(letters) - 1][:len(letters[len(letters) - 1]) - 1]

#edge case: empty set
if letters[0] == '':
    print(0)
    quit()

print(len(set(letters)))