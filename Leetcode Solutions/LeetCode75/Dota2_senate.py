# problem link: https://leetcode.com/problems/dota2-senate


# my solution:
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        
        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + len(senate))
            else:
                dire.append(dire[0] + len(senate))
            radiant.pop(0)
            dire.pop(0)
        
        return 'Radiant' if len(radiant) > len(dire) else 'Dire'
