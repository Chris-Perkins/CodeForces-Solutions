# Description of problem can be found at http://codeforces.com/problemset/problem/96/A


def main():
    formation = input()
    
    # If there's not even 7 people, we don't need to check.
    if(len(formation) < 7):
        print("NO")
        quit()
        
    current_tally = 0
    last_seen = None
    
    for team_member in formation:
        # if this team member is from the last team seen
        if team_member == last_seen:
            current_tally += 1
            
            # if this formation is dangerous
            if current_tally == 7:
                print("YES")
                quit()
        
        else:
            last_seen = team_member
            current_tally = 1
    
    print("NO")
    

if __name__ == "__main__":
    main()