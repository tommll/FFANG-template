"""
Problem link: https://leetcode.com/problems/subarray-product-less-than-k/

Idea:

Time complexity:

Space Complexity:
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] < k else 0

        ans = 0
        cur_product = 1
        left = 0

        for right in range(len(nums)):
            cur_product *= nums[right]
            
            while cur_product >= k:
                cur_product /= nums[left]
                left += 1
            
            if left <= right:
                ans += 1 + (right - left)
        return ans
        

