# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        List = []
        while head.next:
            List.append(head.val)
            head = head.next
        List.append(head.val)
        n = len(List) / 2
        if len(List) == 1:
            return True
        if len(List) % 2 == 1:
            return True if List[:n][::-1] == List[n + 1:] else False
        else:
            return True if List[:n][::-1] == List[n:] else False


