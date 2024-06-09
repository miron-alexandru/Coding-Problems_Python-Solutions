# problem link: https://leetcode.com/problems/find-common-characters/


# my solution:
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = Counter(words[0])

        for word in words[1:]:
            word_counter = Counter(word)
            common_counter &= word_counter

        common_letters = list(common_counter.elements())
        
        return common_letters