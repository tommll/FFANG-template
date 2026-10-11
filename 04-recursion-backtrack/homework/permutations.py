class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current_sol = []
        ans = []

        def choose(i, candidates):
            if i == len(nums):
                ans.append(current_sol[:])
                return
            
            for j, x in enumerate(candidates):
                current_sol.append(x)
                choose(i+1, candidates[:j] + candidates[j+1:])
                current_sol.pop()
        
        choose(0, nums)
        return ans




