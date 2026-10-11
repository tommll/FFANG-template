# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Idea: is_ancestor_of_pq(node) --> (bool, bool) = (_1, _2)
        # _1 = true nếu node là ancestor của p, _2 = true nếu ndoe là ancestor của q
        # node._1 = (node.left._1 or node.right._1 or node == p)
        # node._2 = (node.left._2 or node.right._2 or node == q)
        # dừng lại ở lần đầu tiên có một node sao cho node._1 và node._2 cùng bằng True

        # TC: O(N), N là số node
        # SC: O(H), H là độ cao của cây

        ans = None
        def is_ancestor_of_pq(node: TreeNode) -> (bool, bool):
            """
            Return whether node is an ancestor of p, and whether node is an ancestor of q
            """
            nonlocal ans
            if node is None:
                return False, False
            
            is_left_p, is_left_q = is_ancestor_of_pq(node.left)
            is_right_p, is_right_q = is_ancestor_of_pq(node.right)
            is_node_p = is_left_p or is_right_p or node == p
            is_node_q = is_left_q or is_right_q or node == q

            if is_node_p and is_node_q and ans is None:
                ans = node
            
            return is_node_p, is_node_q
        
        _, _ = is_ancestor_of_pq(root)
        return ans


