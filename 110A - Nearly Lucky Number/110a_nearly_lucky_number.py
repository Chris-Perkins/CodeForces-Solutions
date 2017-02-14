# Description of the problem can be found at http://codeforces.com/problemset/problem/110/A


def main():
    lucky_nums = list([4, 7])
    lucky_num_count = 0
    
    in_num = int(input())
    
    while in_num > 0:
        # keep going down the list of numbers
        num_at_end = in_num % 10
        in_num //= 10
        
        for lucky_num in lucky_nums:
            if lucky_num == num_at_end:
                lucky_num_count += 1
                break
            
    for lucky_num in lucky_nums:
        if lucky_num_count == lucky_num:
            print("YES")
            quit()
    
    print("NO")
    

if __name__ == "__main__":
    main()