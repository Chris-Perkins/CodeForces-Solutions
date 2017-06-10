# Description of the problem can be found at http://codeforces.com/problemset/problem/119/A

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def main():
    a, b, n = map(int, input().split())
    
    while n >= 0:
        n -= gcd(a, n)
        if n < 0:
            print("1")
            quit()
        
        n -= gcd(b, n)
        if n < 0:
            print("0")
            quit()


if __name__ == "__main__":
    main()