# problem link: https://leetcode.com/problems/construct-string-with-repeat-limit/description/


# solution (from AlgoMonster):
class Solution:
    def repeatLimitedString(self, s: str, repeat_limit: int) -> str:
        # Initialize a list to keep track of the count of each character
        char_count = [0] * 26
      
        # Count the occurrences of each character in the input string s
        for c in s:
            char_count[ord(c) - ord('a')] += 1
      
        # Initialize a list to build the answer string
        answer = []
      
        # Iterate over characters from 'z' to 'a'
        for i in range(25, -1, -1):
            # Find the next character to place if we hit the repeat limit
            next_char_index = i - 1
          
            # Keep placing characters until we run out
            while True:
                # Place the current character (up to the repeat limit) in the answer
                for _ in range(min(repeat_limit, char_count[i])):
                    char_count[i] -= 1
                    answer.append(chr(ord('a') + i))
              
                # If we have placed all instances of the current character, move to the next
                if char_count[i] == 0:
                    break
              
                # Find the next highest character which we haven't exhausted
                while next_char_index >= 0 and char_count[next_char_index] == 0:
                    next_char_index -= 1
              
                # If there are no more characters to use, we are done
                if next_char_index < 0:
                    break
              
                # Place the next character
                char_count[next_char_index] -= 1
                answer.append(chr(ord('a') + next_char_index))
      
        # Return the constructed string
        return ''.join(answer)