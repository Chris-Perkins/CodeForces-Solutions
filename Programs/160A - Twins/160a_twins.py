# Description of the problem can be found at http://codeforces.com/problemset/problem/160/A


def main():
	# We do not need the first line
	_ = input()
	
	# Get the list of coins, and sort them.
	coins = list(map(int, input().split()))
	coins.sort()
	
	min_coins = 0
	cur_count = 0
	low = 0
	high = len(coins) - 1
	
	while low <= high:
		if cur_count - coins[low] > 0:
			cur_count -= coins[low]
			low += 1
		else:
			cur_count += coins[high]
			min_coins += 1
			high -= 1
	
	print(min_coins)
	
	
if __name__ == "__main__":
	main()