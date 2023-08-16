# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Understand
    
    1 2 3 4 
    -> 1 4 2 3
    
    1 2 3 4 5
    -> 1 5 2 4 3
    
    1 2 3 4 5 6
    -> 1 6 2 5 3 4
    
    Match
    Linked List
    
    Plan
    - multi-pass, two-pointer
    - first pass: slow pointer, fast pointer (2x) --> determine midpoint
    - split LL into two halves and reverse right half of linked list  
    - while right node is not None:
        - left -> right
        - right -> left.next
        - increment left, right
    
    """
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now at midpoint
        
        
        curr = slow.next
        prev = None
        slow.next = None
       # reverse right half of LL
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        left = head
        right = prev
        
        while right:
            left_temp = left.next
            right_temp = right.next
            left.next = right
            right.next = left_temp
            left = left_temp
            right = right_temp
        