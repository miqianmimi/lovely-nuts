# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        a = head
        num = []
        num.append(a.val)
        while a.next:
            a = a.next
            num.append(a.val)

        print(num)
        i = len(num) - 1
        b = head
        b.val = num[i]
        while b.next:
            b = b.next
            i = i - 1
            b.val = num[i]
        return head

    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
