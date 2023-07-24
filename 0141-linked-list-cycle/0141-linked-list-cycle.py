# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    Understand
    
    1->2->3->4->2
    True
    
    1->2->1
    True
    
    1->2
    False
    
    1->
    False
    
    Match
    LinkedList
    
    Plan
    - naive: single pointer, add nodes to encountered list, return true if encounter duplicate node; repeat while current node is not None
    - create encountered set
    - set pointer to head
    - if node is in encountered, return false; else, add node to encountered and increment pointer
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        encountered = set()
        while head:
            if head in encountered:
                return True
            encountered.add(head)
            head = head.next
        return False
        