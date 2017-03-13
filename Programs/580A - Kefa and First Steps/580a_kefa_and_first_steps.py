# Description of the problem can be found at http://codeforces.com/problemset/problem/580/A

last_earned = 0
cur_sequence = 0
max_sequence = 0

_ = input()

days = list(map(int, input().split()))

for earned_in_day in days:
	if earned_in_day >= last_earned:
		cur_sequence += 1
		
		if cur_sequence > max_sequence:
			max_sequence = cur_sequence
	else:
		# cur_sequence is now equal to this sequence
		cur_sequence = 1
	last_earned = earned_in_day
	
print(max_sequence)
		