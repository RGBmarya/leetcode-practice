# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Understand
    
    1 2 3
    4 5 6
    -> 5 7 9
    
    7 3 5
    4 2 3
    -> 1 6 8
    
    0
    0
    -> 0
    
    3 4 5
    2 4 7
    -> 5 8 2 1
    
    2 3
    9 9 3
    -> 1 3 4
    
    Match
    Linked list
    
    Plan
    - dummyhead for result LL
    - set pointers on both LL to head
    - while either node is valid
        - add values of nodes + add carry
        - if one of nodes is None, replace with 0
        - // 10 to determine if need to carry the 1 (could be 0 if <= 10)
        - add node to dummyhead
        - increment the dummyhead, l1, l2
    - return 
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        res = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            place_sum = v1 + v2 + carry
            carry = place_sum // 10
            res.next = ListNode(place_sum % 10)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
            