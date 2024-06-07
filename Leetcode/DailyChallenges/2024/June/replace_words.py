# problem link: https://leetcode.com/problems/replace-words/


# my solution:
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        dictionary_set = set(dictionary)

        def replace(word):
            # Check if any prefix of the word is in the root set
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in dictionary_set:
                    return prefix
            return word

        words = sentence.split()
        # Replace each word with its root
        replaced_words = [replace(word) for word in words]
        # Join the words back
        return ' '.join(replaced_words)