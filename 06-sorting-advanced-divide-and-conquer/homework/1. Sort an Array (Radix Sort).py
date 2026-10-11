"""
Problem Link: https://leetcode.com/problems/sort-an-array/

Idea:

Time complexity:

Space Complexity:
"""

from collections import Counter

class Solution:
    def sortArray(self, nums):
        count_map = Counter(nums)

        idx = 0
        for num in range(min(nums), max(nums) + 1):
            while count_map[num]:
                nums[idx] = num
                idx += 1
                count_map[num] -= 1
        
        return nums

