# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            iterations = len(queue)
            first = True
            for i in range(iterations):
                node = queue.popleft()
                if node:
                    if first:
                        res.append(node.val)
                        first = False
                    queue.append(node.right)
                    queue.append(node.left)
        return res