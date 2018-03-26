# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        List = []
        while head:
            List.append(head.val)
            head = head.next
        print(List)

        if len(List) == 0:
            return None

        def quicksort(List):
            if len(List) <= 1:
                return List
            print(List)
            p = List.pop()
            left = []
            right = []
            for i in range(len(List)):
                if List[i] > p:
                    right.append(List[i])
                elif List[i] < p:
                    left.append(List[i])
            print(left, right)
            return quicksort(left) + [p] + quicksort(right)

        List.sort()
        print(List)
        startt = start
        start.val = List[0]
        for i in range(1, len(List)):
            start.next = ListNode(List[i])
            start = start.next
        start.val = List[-1]

        return startt

