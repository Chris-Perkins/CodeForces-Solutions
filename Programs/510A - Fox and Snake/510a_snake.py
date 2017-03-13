# Description of the problem can be found at http://codeforces.com/problemset/problem/510/A

# get y and x variables
y, x = map(int, input().split())

for y_index in range(y):
    for x_index in range(x):
        # if we're on a "body" line
        if y_index % 2 == 0:
            print("#", end = "")
        else:
            # if we're on a second line and at the last position
            if y_index % 4  == 1 and x_index == x - 1:
                print("#", end = "")
            # if we're on a fourth line and in the first position
            elif y_index % 4 == 3 and x_index == 0:
                print("#", end = "")
            else:
                print(".", end = "")
    # new line
    print()