class SNode:
    def __init__(self, start, end, left, right, range_val):
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.range_val = range_val


class SegmentTree:
    def __init__(self, arr, op):
        self.arr = arr
        self.op = op
        self.tree = self.build_segment_tree()

    def build_segment_tree(self):
        arr = self.arr
        op = self.op

        def build(start, end):
            if start == end:
                return SNode(start, end, None, None, arr[start])
            else:
                mid = (start + end) // 2
                left = build(start, mid)
                right = build(mid + 1, end)
                range_val = op(left.range_val, right.range_val)
                return SNode(start, end, left, right, range_val)

        return build(0, len(arr) - 1)

    def get_range(self, s=None, e=None):
        def range_op(node, start=None, end=None):
            start = start if not None else node.start
            end = end if not None else node.end
            if start == node.start and end == node.end:
                return node.range_val
            elif end < node.right.start:
                return range_op(node.left, start, end)
            elif start > node.left.end:
                return range_op(node.right, start, end)
            else:
                l_range = range_op(node.left, start, node.left.end)
                r_range = range_op(node.right, node.right.start, end)
                return self.op(l_range, r_range)

        return range_op(self.tree, s, e)

    def update(self, i, v):
        op = self.op

        def update(node):
            if node.start == node.end == i:
                self.arr[i] = v
                node.range_val = v
            elif i < node.right.start:
                left = update(node.left)
                node.range_val = op(left.range_val, node.right.range_val)

            else:
                right = update(node.right)
                node.range_val = op(node.left.range_val, right.range_val)

            return node

        update(self.tree)


def main():
    arr = [1, 3, 5]
    segment_tree = SegmentTree(arr, lambda x, y: x + y)
    v = segment_tree.get_range(0, 2)
    print(v)
    segment_tree.update(1, 2)
    v = segment_tree.get_range(0, 2)
    print(v)


if __name__ == "__main__":
    main()
