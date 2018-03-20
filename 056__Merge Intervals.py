class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []

        intervals.sort(key=lambda x: x.start)
        print(intervals)
        intervalnew = []
        n = len(intervals)
        if n == 1:
            return (intervals)
        i = 0
        while i <= n - 2:
            a = i
            # import pdb;pdb.set_trace()
            max = intervals[a].end
            while i <= n - 2 and max >= intervals[i + 1].start:
                i = i + 1
                if intervals[i].end > max:
                    max = intervals[i].end
                if i == n - 1:
                    break
            b = i
            print(b)
            # print(a,b)
            intervalnew.append([a, b])
            i = i + 1
        print(intervalnew)
        complete = []
        for i in range(len(intervalnew)):
            max = intervals[intervalnew[i][0]].end
            for pp in range(intervalnew[i][0], intervalnew[i][1] + 1):
                if intervals[pp].end > max:
                    max = intervals[pp].end
            start, end = intervals[intervalnew[i][0]].start, max
            complete.append([start, end])

        if intervalnew[-1][1] <= n - 2:
            complete.append([intervals[-1].start, intervals[-1].end])
        print(complete)
        return (complete)


class Solution2:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out
a=Solution()
c=Interval(1,3)
d=Interval(2,6)
e=Interval(8,10)
f=Interval(15,18)


b=a.merge([c,d,e,f])
print(b)