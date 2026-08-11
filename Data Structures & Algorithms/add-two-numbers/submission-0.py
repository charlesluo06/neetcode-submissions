# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy


        carry = 0
        while l1 or l2 or carry: #iterate while at least 1 list is valid, OR we have a carry still
            #make sure list vals exist, if not 0
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0

            #new digit
            val = v1 + v2 + carry
            #15
            carry = val // 10 #check if carry
            val = val % 10    #compute the ones
            curr.next = ListNode(val)

            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next