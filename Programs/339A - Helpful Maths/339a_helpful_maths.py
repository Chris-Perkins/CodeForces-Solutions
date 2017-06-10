# Description of problem found at http://codeforces.com/problemset/problem/339/A


def main():
    input_string = input()
    number_input = list()
    
    cur_index = 0
    
    # add to our list of numbers
    while cur_index <= len(input_string):
        number_input.append(input_string[cur_index])
        cur_index += 2
    
    # sort in non-ascending order
    number_input.sort()
    
    for i in range(len(number_input)):
        print(number_input[i], end="")
        if(i + 1 < len(number_input)):
            print("+", end="")
    
    
if __name__ == "__main__":
    main()