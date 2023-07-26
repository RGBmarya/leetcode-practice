# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    """
    Understand
    
    1 2 2 2 3 3 4
    -> 1 4
    
    1 2 3 4
    -> 1 2 3 4
    
    1 2 3 5 5
    -> 1 2 3
    
    Match
    Linked list + hashset
    
    Plan
    - pointer begins at head
    - check if cur node is same is next node
    - if yes
        - increment pointer until cur node is diff from next node
        - connect prev to next
    - else
        - increment prev
    - increment pointer
    
        
        
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
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
