# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current, stack = root, []
        res = []
        while current or stack:
            if current:
                res.append(current.val)
                stack.append(current.right)
                current = current.left
            else:
                current = stack.pop()
        return res
        