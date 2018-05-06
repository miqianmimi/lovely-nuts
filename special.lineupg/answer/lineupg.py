#!/usr/bin/env python2.7

def main():
    height =[]
    queries = []

    with open('lineupg2.in', 'r') as fin:
        n, q = map(int, fin.readline().split(' '))
        for i, line in enumerate(fin):
            if i < n:
                height.append(line.strip())
            else:
                queries.append(line.strip())
    #print(queries)

    height = [int(h, 10) for h in height]
    query=[]


    def find(a,i,j,min,max):
        if i >= j - 1:
            if a[i] > a[j]:
                if min>a[j]:
                    min=a[j]
                if max<a[i]:
                    max=a[i]
                return min,max
            else:
                if min > a[i]:
                    min = a[i]
                if max < a[j]:
                    max = a[j]
                return min,max

        else:
            mid = int((i + j) / 2)
            tmpmin,tmpmax=find(a, i, mid, min,max)
            min,max=find(a, mid + 1, j, min,max)
            min = tmpmin if tmpmin < min else min
            max = tmpmax if tmpmax > max else max
            return min,max

    for q in queries:
        a=q.split(' ')
        l=[]
        for i in a:
            l.append(int(i))
        query.append(l)
    fout = open('lineupg.out', 'w')
    for q in query:
        l = q[0] - 1
        r = q[1]-1
        min,max=find(height,l,r,100000,-100000)
        #import pdb;pdb.set_trace()
        #print (max,min)
        ans = max-min
        print(ans)
        fout.write(str(ans) + '\n')

if __name__ == '__main__':
    main()
