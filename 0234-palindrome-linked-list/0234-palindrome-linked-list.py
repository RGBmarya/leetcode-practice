"""
Understand
1 -> 2 -> 3 -> 2 -> 1

Match
LL

Plan
slow, fast pointer (2x) to find the midpoint
reverse right half of LL
compare values on both LL: 
    while both nodes valid:
    if values differ, return False
    else, increment nodes
    return True

Evaluate
Time: O(n / 2 + n / 2 + n / 2) ~ O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(-1, head)
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev, curr = None, slow.next
        slow.next = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True