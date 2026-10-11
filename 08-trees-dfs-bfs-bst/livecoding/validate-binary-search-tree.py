# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Ý tưởng: Kiểm tra tính chất BST ở từng node. Để kiểm tra tính chất BST ở node u,
        # thì cần kiểm tra xem u có lớn hơn max bên nhánh trái, và có bé hơn min bên nhánh phải
        # của nó hay không.
        # Để tính được min nhánh trái và max nhánh phải, thì ta cẩn sử dụng kết quả đệ quy ở 
        # u.left và u.right
        # min_max_of_subtree(u) --> (int, int) = (u_min, u_max)
        # u_min = min(u_left_min, u.val)
        # u_max = max(u_right_max, u.val)
        # if u.val <= u_left_max or u.val >= u_right_min: --> return False

        # TC: O(N)
        # SC: O(H)

        ans = True
        def min_max_of_subtree(u: TreeNode) -> (int, int):
            """
            Return min and max of all nodes of the subtree rooted at u
            """
            nonlocal ans
            if u is None:
                return (float('inf'), float('-inf'))
            
            min_left, max_left = min_max_of_subtree(u.left)
            min_right, max_right = min_max_of_subtree(u.right)
            if u.val <= max_left or u.val >= min_right:
                ans = False
            
            min_u = min(min_left, u.val)
            max_u = max(max_right, u.val)
            return min_u, max_u
        
        _, _ = min_max_of_subtree(root)
        return ans



