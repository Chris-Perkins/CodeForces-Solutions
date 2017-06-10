# Description of the problem can be found at http://codeforces.com/problemset/problem/266/B


def main():
	num_kids, time = map(int, input().split())
	kids = input()
	
	for i in range(time):
		kids = kids.replace("BG", "GB")
	
	print(kids)
	

if __name__ == "__main__":
	main()