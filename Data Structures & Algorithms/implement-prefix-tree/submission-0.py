class TreeNode:
    def __init__(self):
        self.children = {}
        self.endHere = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if not (char in current.children):
                current.children[char] = TreeNode()
            current = current.children[char]
        current.endHere = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endHere

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

        
        