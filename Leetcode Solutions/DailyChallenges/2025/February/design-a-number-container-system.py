# problem link: https://leetcode.com/problems/design-a-number-container-system




# solution:
class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        # Remove the index from the old number if it exists
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_indices[old_number].remove(index)
        # Update with the new number
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        indices = self.number_to_indices[number]
        return indices[0] if indices else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)