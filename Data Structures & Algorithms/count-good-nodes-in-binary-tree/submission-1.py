# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,root.val)]
        goodNodes = 0
        while stack:
            node, maxUpNow = stack.pop()
            if node.val >= maxUpNow:
                goodNodes += 1
            newMax = max(maxUpNow,node.val)

            if node.right:
                stack.append((node.right,newMax))
            if node.left:
                stack.append((node.left,newMax))
        return goodNodes