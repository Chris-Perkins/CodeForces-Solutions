# Description of problem found at http://codeforces.com/problemset/problem/118/A


def main():
    out_word = ""
    in_word = input().lower()
    
    # Just learned len() is O(1)! neat.
    for character in in_word:
        # if this is not a vowel, add it to our output string
        if not is_vowel(character):
            out_word += "." + character
    
    print(out_word)


# Checks whether a character is a vowel
def is_vowel(character):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    
    # Check whether or not our character is a vowel
    if character in vowel_list:
        return True
    
    return False


if __name__ == "__main__":
    main()