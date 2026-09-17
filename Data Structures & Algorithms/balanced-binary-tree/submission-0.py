# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0] #empty balanced tree

            left, right = dfs(root.left), dfs(root.right) #calling dfs on both subtrees

            #from root is it balanced?
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])] #is whole tree balanced?, height of tree

        return dfs(root)[0] #call dfs (returning the boolean value)