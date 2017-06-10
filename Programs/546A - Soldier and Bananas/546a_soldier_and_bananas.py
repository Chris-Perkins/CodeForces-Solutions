# Description of the problem can be found at http://codeforces.com/problemset/problem/546/A


def main():
    k, n, w = map(int, input().split())
    
    # multiply the cost times the summation
    cost = (k * w * (w + 1)) // 2
    
    if cost <= n:
        print("0")
    else:
        print(cost - n)
    
    
if __name__ == "__main__":
    main()