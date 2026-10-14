# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0
        def dfs(root):
            if root is None:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            
            BF = abs(leftHeight - rightHeight)

            if BF > 1:
                self.res = -1

            return max(leftHeight, rightHeight) + 1
        dfs(root)
        
        if self.res == -1:
            return False
        
        return True