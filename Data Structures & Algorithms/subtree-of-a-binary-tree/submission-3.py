# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root: return False

        def check(tree, subTree):
            if not tree and not subTree:
                return True
        
            if not tree or not subTree:
                return False

            return tree.val == subTree.val and check(tree.right, subTree.right) and check(tree.left, subTree.left) 
            
        if check(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)    