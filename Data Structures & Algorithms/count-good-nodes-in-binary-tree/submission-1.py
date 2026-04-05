# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0            
    #     self.ans = 0
    #     self.dfs(root,root.val)
    #     return self.ans
    
    # def dfs(self,node, val):
    #     if not node:
    #         return 
            
    #     if node.val >= val:
    #         val = node.val
    #         self.ans += 1

    #     if node.left:
    #         self.dfs(node.left,val)
    #     if node.right:
    #         self.dfs(node.right,val)

        if not root:
            return 0

        self.ans = 0

        def dfs(node, maxVal):
            if not node:
                return
            
            if node.val >= maxVal:
                # print(node.val, maxVal)
                self.ans+=1

            dfs(node.left, max(node.val, maxVal))
            dfs(node.right, max(node.val, maxVal))

        dfs(root,root.val)
        return self.ans

