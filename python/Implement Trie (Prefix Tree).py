from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = defaultdict(TrieNode)
        self.isWord = False
        

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cursor = self.root
        for char in word:
            cursor = cursor.nodes[char]
        cursor.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cursor = self.root
        for char in word:
            if char not in cursor.nodes:
                return False
            cursor = cursor.nodes[char]
        return cursor.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cursor = self.root
        for char in prefix:
            if char not in cursor.nodes:
                return False
            cursor = cursor.nodes[char]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
