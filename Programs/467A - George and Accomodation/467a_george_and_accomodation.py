# Description of the problem can be found at http://codeforces.com/problemset/problem/467/A


def main():
    num_rooms = int(input())
    
    available_rooms = 0
    
    for _ in range(num_rooms):
        in_room, allowed = map(int, input().split())
        
        if allowed - in_room >= 2:
            available_rooms += 1
    
    print(available_rooms)
    

if __name__ == "__main__":
    main()