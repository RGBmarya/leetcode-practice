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
        - increment node, update prev
    
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
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            if next_node != None:
                head = next_node
            else:
                return head
        return head
        