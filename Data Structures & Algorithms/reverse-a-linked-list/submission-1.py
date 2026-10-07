# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        start = True
        while head:
            print("r")
            start = False
            tmp = node
            node, head = head, head.next
            node.next = tmp
        return node