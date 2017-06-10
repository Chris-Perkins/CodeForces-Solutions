# Description of the problem can be found at http://codeforces.com/problemset/problem/112/A
# sure, I could do a simple string compare. That goes against the spirit of the problem, though.


def main():
    str1, str2 = input().lower(), input().lower()
    print(compare_strings(str1, str2, 0))


def compare_strings(str1, str2, pos):
    if pos >= len(str1):
        return 0
    elif str1[pos] < str2[pos]:
        return -1
    elif str1[pos] > str2[pos]:
        return 1
    else:
        return compare_strings(str1, str2, pos + 1)


if __name__ == "__main__":
    main()