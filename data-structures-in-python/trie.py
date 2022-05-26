"""
Trie is an efficient information retrieval data structure. Using Trie, search complexities can be brought to optimal
limit (key length).

https://www.geeksforgeeks.org/trie-insert-and-search/
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node, just marks leaf node
        pointer = self.root

        for level in range(len(key)):
            index = self._char_to_index(key[level])

            # if current character is not present
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()

            pointer = pointer.children[index]

        # mark last node as leaf
        pointer.is_end_of_word = True

    def search(self, key):
        # Returns true if key is present in trie, else false
        pointer = self.root

        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]

        return pointer.is_end_of_word


def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()