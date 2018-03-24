# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        walk=ListNode()
        run=ListNode()
        walk =head
        run=head
        while run.next and run.next.next :
            walk=walk.next
            run=run.next.next
            if walk==run:
                return True
        return False

#Use two pointers, walker and runner.
#walker moves step by step. runner moves two steps at time.
#if the Linked List has a cycle walker and runner will meet at some point.