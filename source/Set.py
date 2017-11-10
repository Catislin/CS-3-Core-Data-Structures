from linkedlist import LinkedList

class Set(object):
    def __init__(self, elements=None):
        self.size = 0
        if elements:
            self.buckets = [LinkedList() for i in range(len(elements))]
            for element in elements:
                self.add(element)
        else:
            self.buckets = [LinkedList() for i in range(8)]

    def __str__(self):
        elements = self.get_elements()
        return '[' + ', '.join(elements) + ']'

    def _bucket_index(self, element):
        """Hashes the element and returns the index of the bucket it is hashed to"""
        return hash(element) % len(self.buckets)

    def _load_factor(self):
        """ Returns the ratio of the number of elements to the number of buckets """
        return self.size / len(self.buckets)

    def get_elements(self):
        return_list = []
        for bucket in self.buckets:
            for element in bucket.iterate():
                return_list.append(element)
        return return_list

    def add(self, element):
        """Adds the specified element only if it is not only present in the Set"""
        if not self.contains(element):
            bucket_index = self._bucket_index(element)
            self.buckets[bucket_index].append(element)
            self.size += 1

    def get(self, element):
        """Returns the specified elements, returns None if not found """
        bucket_index = self._bucket_index(element)
        return self.buckets[bucket_index].find(lambda value: value == element)

    def contains(self, element):
        bucket_index = self._bucket_index(element)
        return self.buckets[bucket_index].find(lambda value: value == element) is not None

    def remove(self, element):
        if self.contains(element):
            bucket_index = self._bucket_index(element)
            bucket = self.buckets(bucket_index)
            bucket.delete(element)
            self.size -= 1

    def is_subset(self, other):
        """Returns true if the first set is a subset of the second"""
        # we want to know if some set, A, is a subset of another set, B
        # go through every element in set A
        for bucket in self.buckets:
            for element in bucket.iterate():
                # if B has an element that A does not, then
                # A is NOT a subset of B
                if not other.contains(element):
                    return False
        # if we do not find an element in B that is not in A, then
        # A must be a subset of B
        return True

    def union(self, other):
        """Given two Sets, return a new Set containing every element in both Sets"""
        # initialize new Set from the elements in the first Set
        union_set = Set(self.get_elements())

        # add every element in the second Set to a new Set and return it
        for element in other.get_elements():
            union_set.add(element)
        return union_set

    def intersection(self, other):
        """ Given two Sets, return a new Set containing only those elements that are in both """
        intersection_set = Set()

        for bucket in self.buckets:
            for element in bucket.iterate():
                if other.contains(element):
                    intersection_set.add(element)
        return intersection_set

    def difference(self, other):
        diff_set = Set()

        for bucket in self.buckets:
            for element in bucket.iterate():
                if not other.contains(element):
                    diff_set.add(element)
        return diff_set


if __name__ == '__main__':
    A = Set(['a', 'b'])
    B = Set(['a', 'b', 'c'])
    A.add('b')
    print(A.is_subset(B)) # True
    print(A.is_subset(A)) # True
    print(B.is_subset(A)) # False

    C = Set(['e', 'z'])
    D = Set(['w', 'x', 'z'])
    print(C.union(D)) # e, x, w, x
    print(C.intersection(D)) # z
    print(C.difference(D)) # e
