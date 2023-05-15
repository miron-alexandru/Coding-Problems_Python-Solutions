# problem link: https://www.hackerrank.com/challenges/separate-the-numbers/problem


# my solution:
def separateNumbers(s):
    # Check if the string starts with '0' or has a length of 1,
    if s[0] == '0' or len(s) == 1:
        print("NO")
        return
    
    # Iterate through possible lengths of the first number
    for i in range(1, len(s)//2 + 1):
        first_num = int(s[:i])
        current_num = first_num
        expected_num = first_num + 1
        remaining_str = s[i:]
        
        # While the remaining substring starts with the expected number:
        # Update the current and expected numbers
        # Update the remaining substring
        while remaining_str.startswith(str(expected_num)):
            current_num = expected_num
            expected_num += 1
            remaining_str = remaining_str[len(str(current_num)):]
        
        # If the remaining substring becomes empty, a beautiful sequence is found
        if remaining_str == '':
            print("YES", first_num)
            return
    
    print("NO")
