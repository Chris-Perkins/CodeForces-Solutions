# Description of problem found at http://codeforces.com/problemset/problem/133/A

def main():
    print_commands = ["H", "Q", "9"]
    
    in_str = input()
    
    for character in in_str:
        for print_command in print_commands:
            if character == print_command:
                print("YES")
                quit()
    
    print("NO")
    
    
if __name__ == "__main__":
    main()