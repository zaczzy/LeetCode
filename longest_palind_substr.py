# this is the trie implementation
from data_structure.trie import TrieNode, Trie
import functools
def insert_suffixes(trie, s):
    for i in range(len(s)):
        trie.insert(s[i:len(s)])


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # insert all suffixes
        trie = Trie()
        insert_suffixes(trie, s+"&")
        s_rev = ''.join(reversed(list(s)))
        insert_suffixes(trie, s_rev+"#")
        # run DFS and return the route to the deepest node with more than 1 child
        # measure of depth should be a parameter to pass to a recursive search
        trie.print()
        return self.deepest_internal_node(trie)

    def deepest_internal_node(self, trie):
        return self.recursive_visit(trie.root)[1][:-1]

    def recursive_visit(self, node):
        if len(node.children) == 0:
            return 0, None
        else:
            results = [self.recursive_visit(node.children[child]) for child in node.children]
            depths = [item[0] for item in results]
            maximum_depth = functools.reduce(lambda max_depth, curr_depth: max(max_depth, curr_depth), depths)
            char_child = results[depths.index(maximum_depth)][1]
            if char_child is not None:
                return maximum_depth, char_child + node.value
            elif len(node.children) > 1:
                return node.depth, node.value
            else:
                return 0, None

if __name__ == "__main__":
    print(Solution().longestPalindrome("aabaab"))