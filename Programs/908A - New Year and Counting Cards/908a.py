flipped_cards = {'a', 'e', 'i', 'o', 'u'}
x = 0
for c in input():
    if c in flipped_cards:
        x += 1
    if c.isdigit() and int(c) % 2 == 1:
        x += 1

print(x)