class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned = {}
        def clone(node):
            if node is None:
                return None
            if node.val not  in cloned:
                newNode = Node(node.val,[])
                cloned[node.val] = newNode
                print(newNode.val)
                neighbors = [clone(x) for x in node.neighbors]
                print([x.val for x in neighbors])
                newNode.neighbors = neighbors
            return cloned[node.val]

        import pdb; pdb.set_trace()
        cln = clone(node)
        return cln

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

one.neighbours = [two,four]
two.neighbours = [one,three]
three.neighbours = [four,two]

sol = Solution()
cloned = sol.cloneGraph(one)
cloned
