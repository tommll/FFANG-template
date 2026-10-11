"""
Problem Link: https://leetcode.com/problems/k-closest-points-to-origin/

Idea:

Time complexity:

Space Complexity:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        slow, fast = head, head
        slow_prev = None
        
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        slow_prev.next = None
        
        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root

       