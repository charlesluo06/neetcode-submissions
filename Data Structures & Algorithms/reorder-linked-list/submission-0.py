# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next #second half of list
        slow.next = None #split the halves

        prev = None #REVERSE 2nd HALF
        while second: 
            next = second.next
            second.next = prev
            prev = second
            second = next

        #merge the lists
        first = head
        second = prev #Second is currently null, need to set to valid node
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2



        