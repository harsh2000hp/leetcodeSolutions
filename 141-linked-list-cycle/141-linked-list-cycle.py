# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodesSeen = set()
        while head is not None:
            if head in nodesSeen:
                return True
            nodesSeen.add(head)
            head = head.next
        return False