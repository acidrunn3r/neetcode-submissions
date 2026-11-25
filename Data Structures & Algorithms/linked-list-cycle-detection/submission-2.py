# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head

        while slow_ptr and fast_ptr:
            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
            else:
                fast_ptr = None

            slow_ptr = slow_ptr.next

            if slow_ptr == fast_ptr != None:
                return True
        
        return False
