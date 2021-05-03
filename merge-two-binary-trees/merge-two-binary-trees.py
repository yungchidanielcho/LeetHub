# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        result = TreeNode()
        if root1 and root2:
            result.val = root1.val + root2.val
            result.left = Solution.mergeTrees(result, root1=root1.left, root2=root2.left)
            result.right = Solution.mergeTrees(result, root1=root1.right, root2=root2.right)
            
        elif root1:
            result.val = root1.val
            if root1.left:
                result.left = Solution.mergeTrees(result, root1 = root1.left, root2 = None)       
            if root1.right:
                result.right = Solution.mergeTrees(result, root1 = root1.right, root2 = None)
        elif root2:
            result.val = root2.val
            if root2.left:
                result.left = Solution.mergeTrees(result, root1 = None, root2 = root2.left)
            if root2.right:
                result.right = Solution.mergeTrees(result, root1 = None, root2 = root2.right)
        else:
            result = None
            
        return result