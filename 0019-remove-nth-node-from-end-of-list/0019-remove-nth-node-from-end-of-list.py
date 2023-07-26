# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Understand
    1->2->3->4->5 n=1
    1->2->3->4

    1->2->3->4->5 n=5
    2->3->4->5

    1->2->3->4->5 n=3
    1->2->4->5

    Match
    Linked-list
    
    Plan
    Multi-pass
    1st pass: get length
    2nd pass: increment pointer length-n times to get to node you want to delete. Keep track of previous node and remove the node you're at. 

    Dummyhead + Two-pointer
    Separate two pointers by n node; once right pointer reaches the end of the list, then the next node is the node that you want to delete. To make it easy to delete the head of a list, use a dummyhead

    Evaluate
    Time: O(n)
    Space: O(1)
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        dummy_head = ListNode(-1)
        dummy_head.next = head
        left = right = dummy_head
        for i in range(n):
            right = right.next
        while right.next != None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy_head.next
