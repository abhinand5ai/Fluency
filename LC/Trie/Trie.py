class Node:

    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_word = False

    def get_char(self):
        return self.char

    def get_child(self, ch: str):
        for child in self.children:
            if child.get_char() == ch:
                return child
        return None

    def insert_child(self, ch: str):
        child = self.get_child(ch)
        if child is not None:
            return child
        else:
            child = Node(ch)
            self.children.append(child)
            return child

    def mark_word(self):
        self.is_word = True



class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node("")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.trie
        for ch in word:
            curr_node = curr_node.insert_child(ch)

        curr_node.mark_word()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.trie
        for ch in word:
            curr_node = curr_node.get_child(ch)
            if curr_node is None:
                return False

        return curr_node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.trie
        for ch in prefix:
            curr_node = curr_node.get_child(ch)
            if curr_node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
param_2 = obj.search("word")
param_3 = obj.startsWith("wo")
