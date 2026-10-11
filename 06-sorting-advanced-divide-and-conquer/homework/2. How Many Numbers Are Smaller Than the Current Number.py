"""
Problem Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Idea:

Time complexity:

Space Complexity:
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * (max(nums) + 1)
        cul = [0] * (max(nums) + 1)
        for num in nums:
            count[num] += 1
        for i in range(len(count)):
            if i == 0:
                cul[i] = count[i]
            else:
                cul[i] = cul[i-1] + count[i]
        
        ans = []
        for num in nums:
            nSmaller = cul[num] - count[num]
            ans.append(nSmaller)
        return ans
       