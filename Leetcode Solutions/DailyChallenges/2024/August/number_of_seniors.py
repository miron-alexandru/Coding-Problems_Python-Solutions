# problem link: https://leetcode.com/problems/number-of-senior-citizens/



# my solution:
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        
        for detail in details:
            age_str = detail[11:13]
            age = int(age_str)

            if age > 60:
                seniors += 1
        
        return seniors