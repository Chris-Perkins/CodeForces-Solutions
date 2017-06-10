# Description of the problem can be found at http://codeforces.com/problemset/problem/148/A


def main():
    damage_numbers = list()
    dragons_hurt = 0
    # add k, l, m, n, d to our damage_numbers list
    damage_numbers.append(int(input()))
    damage_numbers.append(int(input()))
    damage_numbers.append(int(input()))
    damage_numbers.append(int(input()))
    
    num_dragons = int(input())
    
    for dragon_num in range(num_dragons):
        for damage_number in damage_numbers:
            if (dragon_num + 1) % damage_number == 0:
                dragons_hurt += 1
                break
    
    print(dragons_hurt)
    
    
if __name__ == "__main__":
    main()