# problem link: https://leetcode.com/problems/coupon-code-validator/


# Description:
"""
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:

code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

 

Example 1:

Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

Output: ["PHARMA5","SAVE20"]

Explanation:

First coupon is valid.
Second coupon has empty code (invalid).
Third coupon is valid.
Fourth coupon has special character @ (invalid).
Example 2:

Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

Output: ["ELECTRONICS_50"]

Explanation:

First coupon is inactive (invalid).
Second coupon is valid.
Third coupon has invalid business line (invalid).
"""


# Solution:
class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        # allowed business lines in required order
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        order_index = {b: i for i, b in enumerate(order)}

        valid = []

        for c, b, active in zip(code, businessLine, isActive):
            # active check
            if not active:
                continue

            # business line check
            if b not in order_index:
                continue

            # code check
            if not c:
                continue
            if not all(ch.isalnum() or ch == "_" for ch in c):
                continue

            valid.append((order_index[b], c))

        # sort by business line order, then code
        valid.sort()

        # return only codes
        return [c for _, c in valid]
