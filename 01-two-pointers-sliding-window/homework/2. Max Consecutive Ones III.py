"""
Problem link: https://leetcode.com/problems/max-consecutive-ones-iii/


Idea:

Time complexity:

Space Complexity:
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        [1,1,1,0,0,0,1]
         ^       ^
        """

        num_zeros = 0
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
                
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            
        return ans
       