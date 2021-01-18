# Definition for a Node.
import unittest
from typing import List, Tuple


class Node(object):
    def __init__(self, val=None, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


class Codec:

    def serialize(self, root: Node) -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        if root is None:
            return "[]"
        else:
            children = " ".join([self.serialize(child) for child in root.children]) if root.children else ""
            return "{0}{1}".format(root.val, "[" + children + "]" if children else "")

    def deserialize(self, data: str) -> Node:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        n: int = len(data)

        def constructChildren(location: int) -> Tuple[int, List[Node]]:
            if location == n:
                return []
            children: List[Node] = []
            val = ""
            while location < n:
                if data[location] == "[":
                    location, constructed_children = constructChildren(location + 1)
                    if val:
                        children.append(Node(val, constructed_children))
                        val = ""
                    else:
                        return location, constructed_children
                elif data[location] == "]":
                    if val:
                        children.append(Node(val, []))
                    return location + 1, children
                elif data[location] == " ":
                    if val:
                        children.append(Node(val, []))
                        val = ""
                    location += 1
                else:
                    val += data[location]
                    location += 1
            if val:
                children.append(Node(val, []))
            return location, children

        _, nodes = constructChildren(0)

        return nodes[0] if nodes else None


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Codec()

    def test_one(self):
        input = "1[3[5 6] 2 4]"
        self.assertEqual(input, self.sol.serialize(self.sol.deserialize(input)))
        self.assertEqual("44", self.sol.serialize(self.sol.deserialize("44")))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
