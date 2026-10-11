# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Ý tưởng: Duyệt DFS, cắt nhánh sớm dựa trên tính chất BST
        # Ở mỗi node, maintain khoảng tìm kiếm [left, right] dựa trên tính chất BST ở các node
        # phía trên nó.
        # Ví dụ, ở dưới node 7 thì các node phải lớn hơn 5 nhưng bé hơn 10 --> [left, right] = [5, 10].
        # Nếu [left, right] và [low, high] không overlap --> return sớm

        # TC: O(N)
        # SC: O(H)
        
        ans = 0
        def dfs(node: TreeNode, left: int, right: int) -> None:
            """
            Traverse the subtree rooted at node
            """
            nonlocal ans
            if node is None:
                return
            
            if left > high and right < low:
                return
            
            if low <= node.val <= high:
                ans += node.val
            
            dfs(node.left, left, node.val)
            dfs(node.right, node.val, right)
        
        dfs(root, float('-inf'), float('inf'))
        return ans

