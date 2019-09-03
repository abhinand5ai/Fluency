import unittest


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def my_cmp(a, b):
    a = str.lower(a)
    b = str.lower(b)
    if len(a) - len(b) != 0:
        return len(b) - len(a)
    else:
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                return -1 if a[i] < b[i] else 1
            elif a[-(i + 1)] != b[-(i + 1)]:
                return -1 if a[-(i + 1)] < b[-(i + 1)] else 1
            i += 1
    return 0


class SolutionTest(unittest.TestCase):

    def test_one(self):
        words = ['laptop', 'Mobile', 'moaile', 'mobize', 'Car']
        self.assertEqual(
            sorted(words, key=cmp_to_key(my_cmp)),
            ['laptop', 'moaile', 'Mobile', 'mobize', 'Car']
        )
