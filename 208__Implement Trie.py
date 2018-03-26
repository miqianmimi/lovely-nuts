class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        way = self.root
        for m in word:
            if m not in way.children:
                way.children[m] = TreeNode()
            way = way.children[m]
        way.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        way = self.root
        for i in word:
            if i not in way.children:
                return False
            way = way.children[i]
        return way.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        way = self.root
        for i in prefix:
            if i not in way.children:
                return False
            way = way.children[i]
        return True




        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)