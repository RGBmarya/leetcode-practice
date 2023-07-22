# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Understand
    1->2->3->4
    2->1->4->3
    
    1->2->3->4->5
    2->1->4->3->5

    Match
    Linked list

    Plan
    Dummyhead
    - dummyhead
    Two-pointer:
    - init: (prev) -> (left) -> (right)
    - right -> left -> original right.next
    - prev -> right
    - update prev, left, right pointers
    - continue while left or left.next is not None
    """

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        dummy = ListNode(-1, head)

        prev = dummy        
        left = head

        while left and left.next:
            right = left.next

            temp = right.next
            right.next = left
            left.next = temp
            prev.next = right

            prev = left
            left = temp

        return dummy.next        