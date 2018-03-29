class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d.setdefault(str(i), 0)
        for i in nums:
            d[str(i)] += 1
        f = zip(d.values(), d.keys())
        f.sort(key=lambda x: x[0], reverse=True)
        # print(f)
        listt = []
        for i in range(k):
            listt.append(int(f[i][1]))
        print(listt)
        return (listt)

    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Use Counter to extract the top k frequent elements
        # most_common(k) return a list of tuples, where the first item of the tuple is the element,
        # and the second item of the tuple is the count
        # Thus, the built-in zip function could be used to extract the first item from the tuple
        import collections
        print(collections.Counter(nums))
        print(collections.Counter(nums).most_common(k))
        print([i[0] for i in collections.Counter(nums).most_common(k)])
        return [i[0] for i in collections.Counter(nums).most_common(k)]