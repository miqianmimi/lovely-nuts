# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l4 = []
        l3 = ListNode(None)
        up = 0
        while l1 and l2:
            temp = l2.val + l1.val + up
            print(temp)
            if temp < 10:
                l4.append(temp)
                l3.val = temp
                l3.next = ListNode(None)
                l3 = l3.next
                l2 = l2.next
                l1 = l1.next
                up = 0
                print('不进位')
            else:
                a = temp - 10
                l4.append(a)
                l3.val = temp - 10
                l3.next = ListNode(None)
                l3 = l3.next
                l2 = l2.next
                l1 = l1.next
                up = 1
                print('进位')
        if l1:
            while l1:
                temp = l1.val + up
                print(temp)
                if temp < 10:
                    l4.append(temp)
                    up = 0
                    print('不进位')
                    l1 = l1.next
                if temp >= 10:
                    l4.append(temp - 10)
                    up = 1
                    print('进位')
                    l1 = l1.next
        elif l2:
            while l2:
                temp = l2.val + up
                print(temp)
                if temp < 10:
                    l4.append(temp)
                    up = 0
                    print('不进位')
                    l2 = l2.next
                if temp >= 10:
                    l4.append(temp - 10)
                    up = 1
                    print('进位')
                    l2 = l2.next

        if up == 1:
            l3.val = 1
            l3.next = ListNode(None)
            l3 = l3.next
            l4.append(1)
        print(l4)
        return (l4)