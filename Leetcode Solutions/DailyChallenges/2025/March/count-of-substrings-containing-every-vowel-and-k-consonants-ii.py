# problem link: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/


# solution:
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def count_valid_substrings(max_consonants: int) -> int:
            vowel_count = Counter()
            total_substrings = 0
            left = 0
            consonant_count = 0
            
            for char in word:
                if char in "aeiou":
                    vowel_count[char] += 1
                else:
                    consonant_count += 1
                
                while consonant_count >= max_consonants and len(vowel_count) == 5:
                    removed_char = word[left]
                    if removed_char in "aeiou":
                        vowel_count[removed_char] -= 1
                        if vowel_count[removed_char] == 0:
                            del vowel_count[removed_char]
                    else:
                        consonant_count -= 1
                    left += 1
                
                total_substrings += left
            
            return total_substrings

        return count_valid_substrings(k) - count_valid_substrings(k + 1)
