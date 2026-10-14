# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, leftLimit, rightLimit):
            if not node:
                return True
            
            if not (node.val > leftLimit and node.val < rightLimit):
                return False
            
            return valid(node.left, leftLimit, node.val) and    valid(node.right,node.val, rightLimit)
        
        return valid(root, float("-inf"), float("inf"))

        