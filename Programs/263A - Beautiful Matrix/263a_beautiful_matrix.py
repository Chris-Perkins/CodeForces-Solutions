# Description of the problem can be found at http://codeforces.com/problemset/problem/263/A


def main():
	# parse each row and find 1
	for i in range(5):
		col_of_one = input().find('1')
		
		# if we found it
		if col_of_one != -1:
			# because our input is space-separated, divide by two.
			col_of_one //= 2
			
			# the amount of transformations to get it to the center x, y
			transformations_x = abs(2 - col_of_one)
			transformations_y = abs(2 - i)
			
			print(transformations_x + transformations_y)


if __name__ == "__main__":
	main()