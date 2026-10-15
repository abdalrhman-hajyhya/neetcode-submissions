# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathForP = []
        pathForQ = []

        def pathForNode(root, target, res):
            if not root:
                return False
            
            res.append(root)
            if root == target:
                return True

            pathLeft = pathForNode(root.left,target,res)
            pathRight = pathForNode(root.right,target,res)

            if not pathLeft and not pathRight:
                res.pop()
                return False
            return True
        
        pathForNode(root,p,pathForP)
        pathForNode(root,q,pathForQ)

        iterations = min(len(pathForP),len(pathForQ))

        for i in range(iterations):
            if pathForP[i] != pathForQ[i]:
                return pathForP[i-1]
        
        return pathForP[iterations - 1]
            
        