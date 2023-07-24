# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    """
    Understand
    1 1 2
    1 2
    
    1 1 2 3 3 
    1 2 3
    
    Match
    Linked List + Hashset
    
    Plan
    - create a dummy, set prev to dummy
    - pointer at the head
    - check if value has been encountered
    - if encountered, connect prev to next, increment pointer and prev
    - if not encountered, add it to encountered hashset, increment pointer and prev
    - repeat while current node is not Null
    
    Evaluate
    Time: O(n)
    Space: O(n) 
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        prev = dummy
        
        encountered = set()
        while head:
            if head.val in encountered:
                prev.next = head.next
            else:
                encountered.add(head.val)
                prev = head
            head = head.next
        return dummy.next
            
        