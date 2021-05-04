# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBalancedhelper( root, height) -> (bool,int):
            if root is None:
                return (True,height)
            height += 1
            is_l_balanced, l_height = isBalancedhelper(root.left,height)
            is_r_balanced, r_height = isBalancedhelper(root.right,height)
            return ((is_l_balanced and is_r_balanced) and (abs(l_height - r_height) <= 1),
                    max(l_height, r_height))
        Balanced, height = isBalancedhelper(root,0)
        return Balanced