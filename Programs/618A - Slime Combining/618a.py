# Description of the problem can be found at http://codeforces.com/problemset/problem/618/A

# in: list of values in non-descending order, the value to search for
#     the first index to check between and the last index to check to
# out: one index of value if it exists. If it does not, return -1
# From: My Common Python Functions library
def binary_search_index_of(value, low, high):
    if low >= high:
        # if this is the value we're looking for, return it.
        if 2**((low + high) // 2) <= value:
            return (low + high) // 2
        elif 2**((low + high) // 2) > value:
            return (low + high) // 2 - 1
    else:
        # get the midpoint between the two functions
        mid = (low + high) // 2
        # if this is greater than value, search the left half
        if 2**mid > value:
            return binary_search_index_of(value, low, mid - 1)
        # if this is less than value, search the right half
        elif 2**mid < value:
            return binary_search_index_of(value, mid + 1, high)
        else:
            return mid

n = int(input())

c = n
while c > 0:
    r = binary_search_index_of(c, 0, 100000)
    c -= 2**r
    print(r + 1, end = " ")