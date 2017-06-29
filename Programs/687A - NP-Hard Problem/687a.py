# Description of the problem can be found at http://codeforces.com/problemset/problem/687/A

from collections import deque


n, m = map(int, input().split())

e = {u : set() for u in range(n)}

for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    e[u].add(v)
    e[v].add(u)

c = {u : 0 for u in range(n)}

dep = set(range(n))

while len(dep) != 0:
    u = dep.pop()
    c[u] = 1
    q = deque([u])
    while len(q) != 0:
        u = q.popleft()
        for v in e[u]:
            if v not in dep:
                if c[v] == c[u]:
                    print(-1);
                    exit();
            else:
                dep.remove(v);
                assert(c[v] == 0);
                c[v] = 3 - c[u];
                q.append(v)
                

a = [u for u in range(n) if c[u]==1]
b = [u for u in range(n) if c[u]==2]


print(len(a))
print(' '.join(map(lambda x: str(x + 1), a)))
print(len(b))
print(' '.join(map(lambda x: str(x + 1), b)))