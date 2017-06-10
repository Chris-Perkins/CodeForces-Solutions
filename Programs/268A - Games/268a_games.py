# Description of the problem can be found at http://codeforces.com/problemset/problem/268/A

num_teams = int(input())
home_colors = list()
guest_colors = list()
num_swaps = 0

for _ in range(num_teams):
    home_color, guest_color = map(int, input().split())
    home_colors.append(home_color), guest_colors.append(guest_color)

for home_index in range(num_teams):
    for guest_index in range(num_teams):
        if home_colors[home_index] == guest_colors[guest_index]:
            num_swaps += 1

print(num_swaps)            