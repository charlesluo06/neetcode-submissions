"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None} # old node null, copy is null
        curr = head

        while curr: #first pass (deep copy)
            copy = Node(curr.val)   #make copy
            oldToCopy[curr] = copy   #map old to copy in hash
            curr = curr.next

        curr = head
        while curr:                              #second pass (linking ptrs)
            copy = oldToCopy[curr]               #copied node
            copy.next = oldToCopy[curr.next]     #update copy next
            copy.random = oldToCopy[curr.random] #update copy random
            curr = curr.next                     #update curr
        return oldToCopy[head]                   #return the copied list's head



        