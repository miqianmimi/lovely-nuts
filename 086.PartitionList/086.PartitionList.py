# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        a = []
        b = []
        if head == None:
            return None
        new_head = head
        while head != None:
            if head.val < x:
                a.append(head.val)
            else:
                b.append(head.val)
            head = head.next
        a.extend(b)
        print(a)
        new_new_head = new_head
        for i in a:
            new_head.val = i
            new_head = new_head.next
        return new_new_head