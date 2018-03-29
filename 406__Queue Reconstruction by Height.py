#首先我们来看一种超级简洁的方法，不得不膜拜想出这种解法的大神。
#首先我们给队列先排个序，按照身高高的排前面，如果身高相同，则第二个数小的排前面。然后我们新建一个空的数组，遍历之前排好序的数组，
# 然后根据每个元素的第二个数字，将其插入到res数组中对应的位置，参见代码如下：

class Solution(object):
    def reconstructQueue(self, people):
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()  # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res
