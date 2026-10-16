class TreeNode:
    def __init__(self):
        self.children = {}
        self.endHere = False
class WordDictionary:
    def __init__(self):
        self.root = TreeNode()
    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TreeNode()
            current = current.children[char]
        current.endHere = True
    def search(self, word: str) -> bool:
        def dfs(index, root):
            current = root
            for i in range(index, len(word)):
                if word[i] == '.':
                    for child in current.children.values():
                        if dfs(i + 1,child):
                            return True
                    return False
                else:
                    if word[i] not in current.children:
                        return False
                    current = current.children[word[i]]
            return current.endHere
        return dfs(0, self.root)