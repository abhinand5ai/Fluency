#!/bin/python3



def count_inversions(arr):
    inversions = [0]

    def sort(array, size):
        if size == 1:
            return  array
        mid = int(size/2)
        return merge(
            sort(array[:mid], mid),
            sort(array[mid:], size - mid),
            mid, size - mid
        )

    def merge(a, b, s_a, s_b):
        i, j = 0, 0
        merged = []
        m = 0
        while i < s_a and j < s_b:
            if a[i] > b[j]:
                merged.append(b[j])
                m += 1
                j += 1
                inversions[0] += s_a + j - m
            else:
                merged.append(a[i])
                m += 1
                i += 1
        if i < s_a:
            merged += a[i:]
        elif j < s_b:
            merged += b[j:]
        return merged
    sorted_list = list(sort(arr, len(arr)))
    print(sorted_list)
    return inversions[0]

def createNode(data):
    pass
def sortedInsert(head, data):
    h = head
    # while node:
    #     print(str(node.data))

    #     node = node.next

    while True:
        if h.next is None and h.data <= data:
            node = createNode(data)
            h.next = node
        if h.prev is None and data < h.data:
            node = createNode(data)
            h.prev = node
        if h.next is not None:
            print()
            if h.next.data < data:
                sortedInsert(h.next, data)
                return
            elif h.data < data <= h.next.data:
                node = createNode(data)
                node.next = h.next
                h.next = node
                return
    return head

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = count_inversions(arr)

        print(str(result) + '\n')

