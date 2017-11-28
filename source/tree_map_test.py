from treemap import TreeMap
import unittest


class TreeMapTest(unittest.TestCase):

    def test_init(self):
        treemap = TreeMap()
        assert treemap.size == 0

    def test_set(self):
        treemap = TreeMap()
        treemap.set('A', 3)
        assert treemap.size == 1
        assert treemap.get('A') == 3
        treemap.set('A', 3)
        assert treemap.size == 1

    def test_contains(self):
        treemap = TreeMap()
        treemap.set('A', 3)
        assert treemap.contains('A')
        assert treemap.contains('B') is False

if __name__ == '__main__':
    unittest.main()
