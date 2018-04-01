class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """


        #Greddy SOLUTION BUT WITH ERRORS
        import collections
        li = collections.Counter(tasks)
        print(li)
        S = []
        idle = 0
        # print(li.most_common())


        for t, i in enumerate(li.most_common()):
            if t == 0:
                # li[i]=i[1]
                # i=i[0]
                cc = [i[0]]
                for m in range(n):
                    cc.append(0)
                # print(cc)
                for j in range(i[1]):
                    S.extend(cc)
            elif t != 0:
                if 0 in S:
                    a = (S.index(0))
                    # print('a=?',a)
                    S[a] = i[0]
                    # print(S)
                    for j in range(1, i[1]):
                        # print(S)
                        print(a + j * (n + 1))
                        if S[a + j * (n + 1)] == 0:
                            S[a + j * (n + 1)] = i[0]
                            # print(S)
                else:
                    for j in range(i[1]):
                        S = S[:t + j * (n + 1)] + [i[0]] + S[t + j * (n + 1):]
        for i in S:
            if S[-1] == 0:
                S.pop()
        print(S)
        return (len(S))


class Solution2(object):
    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        task_counts = collections.Counter(tasks).values()
        print(task_counts)
        M = max(task_counts)
        print(M)#最大值
        MCT = task_counts.count(M)
        print(MCT)#有几个
        return max(len(tasks), (M - 1) * (n + 1) + MCT)