# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        queue = collections.deque()
        queue.append([root,float("-inf"),float("inf")])

        while queue:
            node, leftLimit, rightLimit = queue.popleft()
            if not(node.val > leftLimit and node.val < rightLimit):
                return False

            if node.left:
                queue.append([node.left,leftLimit,node.val])
            if node.right:
                queue.append([node.right,node.val,rightLimit])
        
        return True