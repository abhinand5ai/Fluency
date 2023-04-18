

###
# The polygons are lists of x,y coordinates, which are the points of the polygons. They are ordered according to the edges of the polygon.
# So if two points are adjacent in the list, there is an edge between them. There is also an edge between the first and the last vertex in the list.
#
# findSharedEdge takes as inputs two polygons, and should return the shared edge iff there is an identical edge contained within both input polygons, otherwise None.

# Example
import itertools

test_poly1 = [(0, 0), (0, 1), (1, 1), (1, 0)]
test_poly2a = [(1, 1), (1, 0), (2, 0)]
test_poly2b = [(2, 0), (1, 0), (1, 1)]
test_poly3 = [(0, 1), (0, 2), (1, 2), (1, 1)]

def pairwise(ls):
    for a, b in zip(ls[:-1], ls[1:]):
        yield (a, b)
    
def findSharedEdge(poly1, poly2):
    poly2_r = list(reversed(poly2))
    poly2_r.append(poly2_r[0])
    poly2.append(poly2[0])
    poly1.append(poly1[0])
    
    
    s2_r = set()
    s2_r.update(list((a, b) for a, b in pairwise(poly2_r)))
    s2 = set()
    s2.update(list((a,b) for a, b in pairwise(poly2)))
    s1 = set()
    s1.update(list((a, b) for a, b in pairwise(poly1)))
    a = s1.intersection(s2)
    if len(a) != 0:
        return list(a)
    b = s1.intersection(s2_r)
    if len(b) != 0:
        return list(b)
    


print(findSharedEdge(test_poly1, test_poly2a)) # ((1, 1), (1, 0))
print(findSharedEdge(test_poly1, test_poly2b)) # ((1, 1), (1, 0))
print(findSharedEdge(test_poly1, test_poly3)) # ((0, 1), (1, 1))
