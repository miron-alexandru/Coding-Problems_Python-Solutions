# problem link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters



# my solution:
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0

        for word in words:
            # Init frequency dicts
            word_freq = {}
            chars_freq = {}
            
            for char in word:
                word_freq[char] = word_freq.get(char, 0) + 1
            
            for char in chars:
                chars_freq[char] = chars_freq.get(char, 0) + 1

            # Check character frequencies
            is_good_word = True
            for char, freq_in_word in word_freq.items():
                if char not in chars_freq or freq_in_word > chars_freq[char]:
                    is_good_word = False
                    break

            # Update sum 
            if is_good_word:
                total_length += len(word)

        return total_length