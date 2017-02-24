# Description of the problem can be found at http://codeforces.com/contest/777/problem/B

card_len = int(input()) - 1
sherlock_card = sorted(input())
moriarty_card = sorted(input())

sherlock_flicked = 0
moriarty_flicked = 0

sherlock_index = card_len
moriarty_index = 0

for index in range(len(moriarty_card)):
    while moriarty_index <= card_len and sherlock_card[index] > moriarty_card[moriarty_index]:
        moriarty_index += 1
    
    if moriarty_index > card_len and moriarty_flicked == 0:
        moriarty_flicked = card_len - index + 1
    
    moriarty_index += 1
    
    while sherlock_index >= 0 and sherlock_card[sherlock_index] >= moriarty_card[card_len - index]:
        sherlock_index -= 1

    if sherlock_index >= 0:
        sherlock_flicked += 1
        sherlock_index -= 1

print(moriarty_flicked)
print(sherlock_flicked)