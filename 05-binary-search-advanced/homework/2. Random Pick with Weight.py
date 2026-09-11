"""
Problem Link: https://leetcode.com/problems/random-pick-with-weight/

Idea:

Time complexity:

Space Complexity:
"""

import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.nums = w
        self.prefixSum = [0] * len(w)
        self.total = sum(w)
        for i, num in enumerate(self.nums):
            if i == 0:               
                self.prefixSum[i] = num
            else:
                self.prefixSum[i] = num + self.prefixSum[i-1]

    def pickIndex(self) -> int:
        rand_num = random.randint(1, self.total)
        pos = bisect.bisect_left(self.prefixSum, rand_num)
        return pos
        


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()