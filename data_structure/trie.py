# Sets membership checks first checks the __hash__, then __eq__
# We should override __hash__, __cmp__ and __eq__
# We can print strings in format using %d, %s, %f
# Overriding __repr__ in python 2.7 allow you to control how python describes the object
# e.g repr(x) return a string description of object x
# Similar effects can be achieved using %r in strings
# TrieNode should use a dictionary for children
# Invariant: never accept None value children
import collections


class Trie(object):
    def __init__(self):
        self.root = TrieNode('*', 0)
        self.max_depth = self.root.depth

    def insert(self, iterable):
        assert isinstance(iterable, collections.Iterable), "Parameter to insert is not iterable."
        current = self.root
        for item in iterable:
            if item is not None:
                current.append_child(item)
                current = current.children[item]
        deep_depth = current.append_child('$')
        if deep_depth > self.max_depth:
            self.max_depth = deep_depth

    def exists(self, iterable):
        assert isinstance(iterable, collections.Iterable), "Parameter to test is not iterable."
        current = self.root
        for item in iterable:
            if not current.has_child(item):
                return False
            current = current.get_child(item)
        return current.has_child('$')

    def print(self):
        layers = {}
        layers = self.visit(self.root, 0, self.max_depth, layers)
        print(layers)

    def visit(self, node, depth, max_depth, layers):
        if depth not in layers:
            layers[depth] = [node.value]
        else:
            layers[depth].append(node.value)
        depth += 1
        for child in node.children:
            self.visit(node.children[child], depth, max_depth, layers)
        return layers


class TrieNode(object):
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.children = {}

    def append_child(self, value):
        assert value is not None, "Appending None TrieNode is not useful."
        if value not in self.children:
            self.children[value] = TrieNode(value, self.depth + 1)
        return self.depth + 1

    def remove_child(self, value):
        assert value is not None, "Cannot remove a None child."
        if value not in self.children:
            raise KeyError("The node you tried to delete is not a child.")
        else:
            self.children.pop(value)

    def has_child(self, value):
        return value in self.children
