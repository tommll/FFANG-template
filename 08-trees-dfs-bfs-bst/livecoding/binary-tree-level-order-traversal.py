# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Ý tưởng: Sử dụng BFS để duyệt cây theo tứ tự từ trên xuống dưới, trái sang phải.
        # Với mỗi node, ta cũng lưu thêm level (a.k.a độ sâu) của node đó.
        # Cùng với đó, ta cũng lưu level của cây hiện tại
        # Khi level của node tiếp theo > level của node hiện tại, ta biết đó là lúc ta đã duyệt
        # đến một level mới --> tạo list mới

        # TC: O(N) 
        # SC: O(N)
        
        if root is None:
            return []

        dq = deque()
        dq.append((root, 0))
        ans = []
        current_level = -1

        while dq:
            node, node_level = dq.popleft()
            if node_level > current_level:
                ans.append([node.val]) # [3] [9] [15]
                current_level = node_level
            else:
                ans[-1].append(node.val)
        
            if node.left:
                dq.append((node.left, current_level + 1))
            if node.right:
                dq.append((node.right, current_level + 1))
        
        return ans
            

