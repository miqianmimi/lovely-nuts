class Solution1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            init = head
            a = head
            b = head.next
            a.val, b.val = b.val, a.val
            while a.next.next != None and b.next.next != None:
                a = a.next.next
                b = b.next.next
                a.val, b.val = b.val, a.val
            return init


class Solution2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            init = head
            a = head
            b = head.next
            a.val, b.val = b.val, a.val
            if a.next.next != None and b.next.next != None:
                temp = self.swapPairs(a.next.next)
                b.next = temp
            return init
