# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        #pending
        if not head or not head.next:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head
        tail.next = head

        for i in range(length-k):
            tail = tail.next 

        new_head = tail.next
        tail.next = None
        return new_head       