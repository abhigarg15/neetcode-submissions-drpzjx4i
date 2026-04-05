# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        self.ans = 0

        if not root :
            return 0


        def getDia(node):
            if not node:
                return 0

            left = getDia(node.left)
            right = getDia(node.right)

            self.ans= max(self.ans, left + right)

            return 1 + max(left,right)


        getDia(root)
        return self.ans