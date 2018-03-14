# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def build(node):
            if not node:
                return 0
            T=build(node.next)+1
            if T>n:
                node.next.val=node.val
            return T
        build(head)
        return head.next

