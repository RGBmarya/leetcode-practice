# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Understand
    
    1 2 4 5
    1 3 4 
    -> 1 1 2 3 4 4 5
    
    1 2 3 4
    5 6 7 8 
    -> 1 2 3 4 5 6 7 8
    
    Match
    Linked List
    
    Plan
    - two pointers, one on each linked list
    - dummyhead 
    - append the smaller of the two node values to the dummyhead LL
    - increment the pointer on the LL whose value was added to the dummyhead LL
    - repeat until the value both LL is None
    - append final elements
    
    Evaluate
    Time: O(n)
    Space: O(m + n)
    """
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        prev = dummy
    
        
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
        
        while list1:
            prev.next = list1
            prev = list1
            list1 = list1.next
        
        while list2:
            prev.next = list2
            prev = list2
            list2 = list2.next
        
        return dummy.next