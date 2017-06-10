# Description of problem can be found at http://codeforces.com/problemset/problem/282/A


def main():
	cur_value = 0

	num_operations = int(input())
	
	# get each operation
	for _ in range(num_operations):
		operation = input()
		
		# only have to check the middle value, since X can only be
		# far left or far right.
		if(operation[1] == "+"):
			cur_value += 1
		else:
			cur_value -= 1
	
	print(cur_value)


if __name__ == "__main__":
	main()