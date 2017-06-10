# Description of problem found at http://codeforces.com/problemset/problem/50/A

def main():
    n, m = map(int, input().split())
    
    # By multiplying, we're essentially seeing how many 2x1 dominoess
    # fit in a line of n*m squares.
    totalSquares = n*m
    
    print(totalSquares // 2)

if __name__ == "__main__":
    main()