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
    
    1->2->3->4->5->6
    False
    
    Match
    LinkedList
    
    Plan
    - naive: single pointer, add nodes to encountered list, return true if encounter duplicate node; repeat while current node is not None
    - create encountered set
    - set pointer to head
    - if node is in encountered, return false; else, add node to encountered and increment pointer
    
    - constant memory: two-pointer approach
    - 
    
    Evaluate
    Time: O(n)
    Space: O(n)
    """
    # Naive
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     encountered = set()
    #     while head:
    #         if head in encountered:
    #             return True
    #         encountered.add(head)
    #         head = head.next
    #     return False
    
    # Constant memory
    
    """
    Plan
    - slow pointer incremented by 1 node each iteration; fast pointer incremented by 2 nodes each iteration
    - return True if node at both pointers is same
    - repeat while current and next fast pointer node are valid (worst case, fast.next.next is None, but won't cause error during update)
    - if loop breaks, return False
    
    Evaluate
    Time: O(n) - Floyd's Tortoise and Hare
    Space: O(1)
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        