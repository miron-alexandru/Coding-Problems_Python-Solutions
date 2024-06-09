# problem link: https://leetcode.com/problems/isomorphic-strings/


# my solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for s_chr, t_chr in zip(s, t):
            # if s_chr exists in s_dict, check if matches to t_chr
            if s_chr in s_dict:
                if s_dict[s_chr] != t_chr:
                    return False
            # if t_chr exists in t_dict, check if matches to s_chr
            elif t_chr in t_dict:
                if t_dict[t_chr] != s_chr:
                    return False
            # if neither of them exist in their dicts, add them
            else:
                s_dict[s_chr] = t_chr
                t_dict[t_chr] = s_chr

        return True