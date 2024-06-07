# problem link: https://leetcode.com/problems/hand-of-straights/


# my solution:
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible by groupSize
        if len(hand) % groupSize != 0:
            return False

        # Count the occurrences of each card
        card_count = Counter(hand)
        
        # Sort the card values to ensure we process cards in ascending order
        sorted_keys = sorted(card_count.keys())

        # Iterate over each card value in sorted order
        for card in sorted_keys:
            # If there are any cards of this value left to use
            if card_count[card] > 0:
                # The number of groups we need to form starting with this card
                count = card_count[card]
                # Try to form groups starting from this card
                for i in range(card, card + groupSize):
                    # If there are not enough cards to form a complete group
                    if card_count[i] < count:
                        return False
                    # Subtract the number of cards used in forming this group
                    card_count[i] -= count

        return True