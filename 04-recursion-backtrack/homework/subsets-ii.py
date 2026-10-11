class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        ans = []
        nums.sort()

        for num in range(1 << len(nums)):
            subset = [nums[i] for i in range(len(nums)) if num >> i & 1]
            key = tuple(subset)
            if key not in seen:
                ans.append(subset)
                seen[key] = True

        
        return ans


