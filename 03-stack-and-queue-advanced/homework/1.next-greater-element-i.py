class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # find first greater items for all items in num2
        stack = []
        ans2 = [-1] * len(nums2)

        for i in reversed(range(len(nums2))):
            x = nums2[i]
            while stack and stack[-1] < x:
                stack.pop()
            
            if stack:
                ans2[i] = stack[-1]
            else:
                ans2[i] = -1
                
            stack.append(x)

        # map first greater items in nums2 back to nums1
        value_to_idx = [0] * (max(nums2) + 1)
        for i, x in enumerate(nums2):
            value_to_idx[x] = i
        
        ans1 = [-1] * len(nums1)
        for i, x in enumerate(nums1):
            ans1[i] = ans2[value_to_idx[x]]
        
        return ans1

            