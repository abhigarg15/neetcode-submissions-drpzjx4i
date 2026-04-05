# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])

        ans = []
        
        while q:
            level_size = len(q)
            tmp = []

            for _ in range(level_size):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(tmp)
        res = []
        for ele in ans:
            # print(ele,ele[-1])
            res.append(ele[-1])


        return res