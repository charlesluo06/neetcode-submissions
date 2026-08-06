# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next: #due to shifting 2 per iteration
            slow = slow.next #shift 1
            fast = fast.next.next #shift 2
            if slow == fast: #if meet return true, else continue
                return True
        return False

        