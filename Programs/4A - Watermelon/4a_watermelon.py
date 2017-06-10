# My solution to 4A - Watermelon.
# Output "YES" if you can divide a watermelon into even-number partitions for two people

w = int(input())

# edge case: w = 2 where you cannot divide into even partitions
if w % 2 == 0 and w != 2:
    print("YES")
else:
    print("NO")