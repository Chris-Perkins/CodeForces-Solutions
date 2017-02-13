# Description of problem found at http://codeforces.com/problemset/problem/158/B


def main():
	# the capacity of the car in people count
	car_size = 4
	# current people count
	cur_people_count = 0
	# current number of cars
	cur_num_cars = 0
	
	# we don't use the first line of input.
	_ = int(input())
	
	# sort our input, then we can go through.
	groups = list(map(int, input().split()))
	groups.sort()
	
	low = 0
	high = len(groups) - 1
	
	while low <= high:
		# if no one is in this car or the car exceeds capacity
		if cur_people_count == 0 or cur_people_count + groups[low] > car_size:
			# start a new car, put the largest group in
			cur_num_cars += 1
			cur_people_count = groups[high]
			high -= 1
		# if you can fit more people in this car
		else:
			# put more people in, increment low by 1
			cur_people_count += groups[low]
			low += 1
	
	print(cur_num_cars)
	

if __name__ == "__main__":
	main()