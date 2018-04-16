### 24. Swap Nodes in Pairs
### Question:
Given a linked list, swap every two adjacent nodes and return its head.
### Example:
```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```
### Analysis:
题目意思是:交换一对指针指向的值，
可以采用递归法和遍历法来做这道题

### 方法1：最简单的遍历方法
```
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        else:
            init=head
            a=head
            b=head.next
            a.val,b.val=b.val,a.val
            while a.next.next!=None and b.next.next!=None:
                a=a.next.next
                b=b.next.next
                a.val,b.val=b.val,a.val
            return init  
 ```
### 方法2：递归
```
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
                temp = self.swapPairs(a.next.next) #递归语句
                b.next = temp
            return init
```
### 本题分类：链表问题，遍历法或者递归法
