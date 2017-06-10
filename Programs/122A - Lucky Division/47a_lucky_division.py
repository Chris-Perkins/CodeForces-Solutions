# Description of the problem can be found at http://codeforces.com/problemset/problem/122/A
# Because input is 1<n<1000, we can manually create our list of lucky numbers.
# Otherwise, I would brute force to find all lucky numbers.


def main():
	lucky_nums = [4, 7, 44, 444, 47, 474, 477, 74, 747, 744]
	number = int(input())
	
	for lucky_num in lucky_nums:
		if number % lucky_num == 0:
			print("YES")
			quit()
	print("NO")


if __name__ == "__main__":
	main()