# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # def valid(node, left, right):
        #     if not node:
        #         return True

        #     if not (left < node.val < right):
        #         return False

        #     return valid(node.left,left, node.val) and valid(node.right,node.val, right)

        # return valid(root,float("-inf"),float("inf"))
        
        # if not root:
        #     return True

        # q = deque([(root,float("-inf"), float("inf"))])

        # while q:
        #     node,left,right = q.popleft()

        #     if not (left < node.val < right):
        #         return False
            
        #     if node.left:
        #         q.append((node.left,left,node.val))
            
        #     if node.right:
        #         q.append((node.right,node.val,right))


        # return True

        if not root:
            return True


        def check(leftMax, node, rightMax):
            if not node:
                return True

            if leftMax <  node.val < rightMax:
                return check(leftMax, node.left, node.val) and check(node.val, node.right, rightMax)
            else:
                return False


        return check(float("-inf"), root, float("inf")) 
