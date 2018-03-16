# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            print('1')
            return(None)
        dummy=M=ListNode(0) #一个返回head~一个返回的是整个list.
        while l1 and l2:
            if l1.val<l2.val:
                print(l1.val)
                M.val=l1.val
                temp=ListNode(0)
                M.next=temp
                M=M.next
                l1=l1.next

            else:
                print(l2.val)
                M.val=l2.val
                temp=ListNode(0)
                M.next=temp
                M=M.next
                l2=l2.next
        if l2:
            M.val=l2.val
            l2=l2.next
            M.next=l2

        elif l1:
            M.val=l1.val
            l1=l1.next
            M.next=l1

        return( dummy )

    def mergetwosort(self,  l1, l2):  # recursive
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergetwosort(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2

def printlistnode(head):
    while head:
        print(head.val)
        head=head.next


def mergesortList(l1,l2): #iterative
    dummy=M=ListNode(0)
    while l1 and l2:
        if l1.val<l2.val:
            M.next=l1 #直接一段段的复制
            l1.next=l1
        else:
            M.next=l2
            l2=l2.next
        M=M.next
    M.next=l1 or l2 #直接一起给上
    return dummy.next  #



a=Solution()
b=a.mergeTwoLists(l1,l2)
printlistnode(b)

