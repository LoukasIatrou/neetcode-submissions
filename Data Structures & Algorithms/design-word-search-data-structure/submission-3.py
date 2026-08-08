class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root 
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
    def search(self, word: str) -> bool:

        def dfs(i,node):
            #Base Case: We have a match
            if len(word) == i:
                return node.end
            #Case 1: We have a char:
            if word[i] != ".":
                if word[i] not  in node.children:
                    return False
                return dfs(i+1,node.children[word[i]])
            #Case 2: We have a "."
            for child in node.children.values():
                if dfs(i+1,child):
                    return True
            return False
        return dfs(0,self.root)


            
