# Description of the problem can be found at http://codeforces.com/problemset/problem/266/A


def main():
    # first input doesn't matter
    _ = input()
    
    # get the stone sequence
    stones = input()
    
    tally = 0
    prev_stone = None
    
    for stone in stones:
        if stone == prev_stone:
            tally += 1
        
        prev_stone = stone
    
    print(tally)


if __name__ == "__main__":
    main()