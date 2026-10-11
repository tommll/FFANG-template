# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Idea: Đệ quy, ở mỗi node, truyền thông tin là tổng giá trị của các node từ gốc 
        # tới nó xuống.
        # dfs(node) --> dfs(node, current_sum)
        # dfs(node.left, current_sum + node.val)
        # dfs(node.right, current_sum + node.val)

        # TC: O(N)
        # SC: O(H)

        ans = False
        def dfs(node: TreeNode, current_sum: int) -> None:
            """
            Visit node and all of its descendants
            """
            nonlocal ans
            if node is None:
                return
            
            if node.left is None and node.right is None: # leaf
                if current_sum + node.val == targetSum:
                    ans = True
            
            dfs(node.left, current_sum + node.val)
            dfs(node.right, current_sum + node.val)

        dfs(root, 0)
        return ans
