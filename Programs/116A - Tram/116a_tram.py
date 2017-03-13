# Description of the problem can be found at http://codeforces.com/problemset/problem/116/A


def main():
	num_lines = int(input())
	
	cur_people = 0
	max_in_train = -1
	
	for _ in range(num_lines):
		people_leaving, people_entering = map(int, input().split())
		cur_people = cur_people - people_leaving + people_entering
		
		if cur_people > max_in_train:
			max_in_train = cur_people
	
	print(max_in_train)
	

if __name__ == "__main__":
	main()