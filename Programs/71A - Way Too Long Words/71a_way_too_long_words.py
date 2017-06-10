# Description of problem found at http://codeforces.com/problemset/problem/71/A


def main():
    times = int(input())
    for _ in range(times):
        print_shortened_word(input())

    
def print_shortened_word(word):
    if len(word) > 10:
        print (word[:1] + str((len(word) - 2)) + word[len(word) - 1])
    else:
        print (word)


# begin our code here  
main()