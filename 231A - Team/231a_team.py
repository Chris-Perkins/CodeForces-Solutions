# Description of problem found at http://codeforces.com/problemset/problem/231/A
# I decided to try and make this program as flexible as problem.
# This removes simplicity, but increases my skill, which is why I'm here


def main():
    num_programs = int(input())
    
    solvable_programs = 0
    
    for _ in range(num_programs):
        tally = 0
        
        friend_answers = list(map(int, input().split()))
        
        for i in range(len(friend_answers)):
            if friend_answers[i] == 1:
                tally += 1
        
        if(tally > len(friend_answers) // 2):
            solvable_programs += 1
    
    print(solvable_programs)
    
    
if __name__ == "__main__":
    main()