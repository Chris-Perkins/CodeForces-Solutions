# Description of the problem can be found at http://codeforces.com/problemset/problem/58/A


def main():
    wanted = "hello"
    in_string = input()
    
    for character in in_string:
        if character == wanted[0]:
            wanted = wanted[1:]
            
            if len(wanted) == 0:
                print("YES")
                quit()
                
                
    print("NO")
    

if __name__ == "__main__":
    main()