# Description of the problem can be found at http://codeforces.com/problemset/problem/236/A


def main():
    in_string = input()
    char_set = set()
    unique_chars = 0
    
    for character in in_string:
        if not char_set.__contains__(character):
            unique_chars += 1
            char_set.add(character)
    
    print("CHAT WITH HER!" if unique_chars % 2 == 0 else "IGNORE HIM!")
    

if __name__ == "__main__":
    main()