"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        current = root
        stack = []
        res = []

        while current or stack:
            if current:
                res.append(current.val)
                if len(current.children) > 0:
                    for i in range(len(current.children) - 1):
                        stack.append(current.children[i])
                    current = current.children[len(current.children) - 1]
                elif stack:
                    current = stack.pop()
                else:
                    break
            else:
                current = stack.pop()
        res.reverse()
        return res