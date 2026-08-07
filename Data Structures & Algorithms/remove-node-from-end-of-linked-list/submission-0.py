# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        while n > 0 and right: #shift right n amount of times
            right = right.next
            n -= 1

        while right:  # shift to end and make left in the correct spot
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummyNode.next
        