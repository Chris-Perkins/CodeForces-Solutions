# Note: This is my first ever Python program. It may look ugly compared to my skill in the future.
# Please look at later programs.

# Get inputs
n,m,a = map(int, raw_input().split())

# My very first ternary operator in Python! Wow they look ugly here.
num_flags_x = n / a + (0 if n % a == 0 else 1)
num_flags_y = m / a + (0 if m % a == 0 else 1)

# Print outputs
print(num_flags_x*num_flags_y)