# Description of the problem can be found at http://codeforces.com/problemset/problem/500/A

num_cells, wanted_cell = map(int, input().split())
portals = list(map(int, input().split()))

cur_cell = 1

# while we have not passed the cell we want
while cur_cell < wanted_cell:
    cur_cell += portals[cur_cell - 1]
        
print("YES" if cur_cell == wanted_cell else "NO")