from linkedlist import LinkedList

class Set(object):
    def __init__(self, elements=None):
        self.size = 0
        if elements:
            self.buckets = [LinkedList() for i in range(len(elements))]
            for element in elements:
                self.add(element)
        else:
            self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        pass

    def _bucket_index(self, item):
        """Hashes the item and returns the index of the bucket it is hashed to"""
        return hash(item) % len(self.buckets)

    def _load_factor(self):
        """ Returns the ratio of the number of items to the number of buckets """
        return self.size / len(self.buckets)

    def get_items(self):
        return_list = []
        for bucket in self.buckets:
            for item in bucket:
                return_list.append(item)
        return return_list


    def add(self, item):
        """Adds the specified item only if it is not only present in the Set"""
        if not self.contains(item):
            bucket_index = self._bucket_index(item)
            self.buckets[bucket_index].append(item)
            self.size += 1

    def get(self, item):
        """Returns the specified items, returns None if not found """
        bucket_index = self._bucket_index(item)
        return self.buckets[bucket_index].find(lambda value: value == item)

    def contains(self, item):
        bucket_index = self._bucket_index(item)
        return self.buckets[bucket_index].find(lambda value: value == item) is not None

    def is_subset(self, other):
        for bucket in self.buckets:
            for item in bucket.iterate():
                if not other.contains(item):
                    return False
        return True

    def union(self, other):
        new_set = Set()





if __name__ == '__main__':
    A = Set(['a', 'b'])
    B = Set(['a', 'b', 'c'])
    A.add('b')
    print(A.is_subset(B))
    print(B.is_subset(A))
