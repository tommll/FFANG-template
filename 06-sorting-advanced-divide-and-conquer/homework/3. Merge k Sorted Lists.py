"""
Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/

Idea:

Time complexity:

Space Complexity:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            node = ListNode()
            ans = node

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            
            if l1:
                node.next = l1
            if l2:
                node.next = l2
            return ans.next
        
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        lists = deque(lists)

        while len(lists) > 1:
            merged_list = merge2Lists(lists.popleft(), lists.pop())
            lists.appendleft(merged_list)
        
        return lists[0]
       