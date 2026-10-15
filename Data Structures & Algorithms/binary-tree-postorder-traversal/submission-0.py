# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            current, case = stack.pop(), visit.pop()
            if current:
                if case:
                    res.append(current.val)
                else:
                    stack.append(current)
                    visit.append(True)
                    stack.append(current.right)
                    visit.append(False)
                    stack.append(current.left)
                    visit.append(False)
        return res
