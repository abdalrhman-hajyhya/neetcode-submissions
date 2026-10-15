# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root : None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
        
        nodeInThePathForP = set()
        while p:
            nodeInThePathForP.add(p)
            p = parent[p]
        
        while q not in nodeInThePathForP:
            q = parent[q]
        return q