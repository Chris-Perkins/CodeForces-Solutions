# Description of the problem can be found at http://codeforces.com/problemset/problem/584/A

def get_num_digits(num):
    digit_count = 0
    
    while num != 0:
        num = num // 10
        digit_count += 1
        
    return digit_count


def main():
    n, t = map(int, input().split())
    
    cur_number = t
    
    while get_num_digits(cur_number) < n:
        cur_number *= t
        
    print(cur_number if get_num_digits(cur_number) == n else -1)
    
    
if __name__ == "__main__":
    main()