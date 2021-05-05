# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaveValues(root:TreeNode) -> list:
            result = []
            queue = []
            queue.append(root)
            def PreOrderTraversal(root:TreeNode,result) -> result:
                currentNode = root
                if currentNode is None:
                    return
                if currentNode.left:
                    result = PreOrderTraversal(root.left,result)
                if currentNode.right:
                    result = PreOrderTraversal(root.right,result)
                if currentNode.left is None and currentNode.right is None:
                    result.append(currentNode.val)
                return result
            result = PreOrderTraversal(root,result)
            return result
        
        leafValue1 = getLeaveValues(root1)
        leafValue2 = getLeaveValues(root2)
        if leafValue1 == leafValue2:
            return True
        else:
            return False
                    