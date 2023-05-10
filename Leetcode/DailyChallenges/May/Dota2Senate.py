# problem link: https://leetcode.com/problems/dota2-senate/submissions


# Solution (not mine) :
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []

        # Divide the senators based on their party and store their indices in separate lists
        for i, party in enumerate(senate):
            if party == "R":
                radiant.append(i)
            else:
                dire.append(i)

        # Continue until either of the parties has no more senators left
        while radiant and dire:
            # Compare the indices of the first senators in both parties' lists
            if radiant[0] < dire[0]:
                # The Radiant senator is at a lower index, so add him to the end of the list with an index that's len(senate) more than his current index
                radiant.append(radiant[0] + len(senate))
            else:
                # The Dire senator is at a lower index, so add him to the end of the list with an index that's len(senate) more than his current index
                dire.append(dire[0] + len(senate))
            # Remove the first senator from both parties' lists since they have exercised their right to ban
            radiant.pop(0)
            dire.pop(0)

        # Return the party with more senators
        return "Radiant" if len(radiant) > len(dire) else "Dire"
