# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = 0

        def isBalanced(root):
            if not root:
                return 0

            right = isBalanced(root.right)
            left = isBalanced(root.left)
            if abs(right-left) > 1:
                self.ans = 1

            return max(left,right) + 1    

        if not root:
            return True

        isBalanced(root)

        return self.ans == 0
