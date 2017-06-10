# Description of problem found at http://codeforces.com/problemset/problem/158/A

def main():
    total = 0
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(n):
        # if this score is greater than the kth place's score and is positive (> 0)
        if arr[i] >= arr[k - 1] and arr[i] > 0:
            total += 1
    
    print(total)

    
main()