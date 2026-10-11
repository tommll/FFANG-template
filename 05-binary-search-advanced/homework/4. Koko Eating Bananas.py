"""
Problem link: https://leetcode.com/problems/koko-eating-bananas/

Idea:

Time complexity:

Space Complexity:
"""

import math

class Solution(object):
    # def minEatingSpeed(self, piles, h):
    #     """
    #     :type piles: List[int]
    #     :type h: int
    #     :rtype: int
    #     """
    
    def can_finish_eating(self, piles, h, k):
        hours_used = 0
        for p in piles:
            hours_used += math.ceil(p / k)

        return hours_used <= h

    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        ans = -1
        while left <= right:
            # print(f"left: #{left}, right: #{right}, ans: #{ans}")
            mid = (left + right) // 2
            if self.can_finish_eating(piles, h, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans       