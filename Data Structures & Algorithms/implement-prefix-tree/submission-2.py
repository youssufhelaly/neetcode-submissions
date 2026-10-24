class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root


        for i in range(len(word)):
            if not word[i] in curr.child:
                return False
            curr = curr.child[word[i]]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in range(len(prefix)):
            if not prefix[i] in curr.child:
                return False
            curr = curr.child[prefix[i]]

        return True



    