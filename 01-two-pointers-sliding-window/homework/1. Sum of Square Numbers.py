"""
Problem Link: https://leetcode.com/problems/sum-of-square-numbers/

Idea:

Time complexity:

Space Complexity:
"""
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        
        for x in range(int(sqrt(c)) + 1):
            remainder = c - x * x
            half = sqrt(remainder)
            if int(half) == half:
                return True

        return False
