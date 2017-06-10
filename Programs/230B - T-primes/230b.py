# Description of the problem can be found at http://codeforces.com/problemset/problem/230/B

input()
primes = [0] * int(1e6)
s = set()
for i in range(2, int(1e6)):
    if not primes[i]:
        s.add(i * i)
        primes[i * i::i] = [1] * len(primes[i * i::i])
        
for i in map(int, input().split()):
    print("YES" if i in s else "NO")