# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, q, p):
        if  (p is None and q is not None) or (p is not None and q is None):
            return False
        elif not q and not p:
            return True
        else:
            if p.val != q.val:
                return False 
        
        
        return (self.isSameTree(p.left,q.left) and   self.isSameTree(p.right,q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def dfs(root, subRoot):
            if root is None:
                return
            if self.isSameTree(root,subRoot):
                self.res = True
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
        dfs(root, subRoot)
        return self.res
        