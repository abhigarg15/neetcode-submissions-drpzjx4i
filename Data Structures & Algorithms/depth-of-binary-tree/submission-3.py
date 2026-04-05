# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], curr: int = 0) -> int:
        
        if not root:
            return curr


        return max(self.maxDepth(root.left,curr+1), self.maxDepth(root.right, curr+1))

