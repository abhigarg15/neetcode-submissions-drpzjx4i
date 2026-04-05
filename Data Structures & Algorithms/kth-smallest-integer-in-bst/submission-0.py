# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.q = []
        def dfs(node):
            if not node:
                return 
            
            self.q.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        heapq.heapify(self.q)

        for i in range(1,k):
            heapq.heappop(self.q)

        return self.q[0]
