# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Understand
    
    1 -> 2 -> 3 -> 4
    4 -> 3 -> 2 -> 1
    
    1 -> 
    1 -> 
    
    []
    []
    
    
    Match
    Linked List
    
    Plan
    - two-pointer approach: prev node, current node
    - While node is not None:
        - set node.next to prev element
        - increment pointer, update prev
    
    Evaluate
    Time: O(n)
    Space: O(1)
    
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        