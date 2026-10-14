# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, maxUpToNow):
            if not root:
                return
            if maxUpToNow <= root.val:
                self.res += 1
            
            maxUpToNow = max(maxUpToNow, root.val)
            dfs(root.left, maxUpToNow)
            dfs(root.right, maxUpToNow)

        dfs(root,root.val)

        return self.res