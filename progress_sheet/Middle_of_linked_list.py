# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        m = head
        li = []
        total = 0
        while m != None:
            m = m.next
            total += 1
            
        if total%2 == 0:
            t = total/2
        else:
            t = (total - 1) / 2
            
        if t == 0:
            return head
        else:
            i = 0
            while i < t:
                head = head.next
                i+=1
                n = head
            
            
        return n
