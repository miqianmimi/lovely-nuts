#!/usr/bin/env python2.7

def main():
    height =[]
    queries = []

    with open('lineupg.in', 'r') as fin:
        n, q = map(int, fin.readline().split(' '))
        for i, line in enumerate(fin):
            if i < n:
                height.append(line.strip())
            else:
                queries.append(line.strip())
    #print(queries)

    height = [int(h, 10) for h in height]
    query=[]
    for q in queries:
        a=q.split(' ')
        l=[]
        for i in a:
            l.append(int(i))
        query.append(l)
    fout = open('lineupg.out', 'w')
    for q in query:
        l = q[0] - 1
        r = q[1]
        ans = max(height[l:r]) - min(height[l:r])
        print(max(height[l:r]) , min(height[l:r]))
        print(ans)
        fout.write(str(ans) + '\n')

if __name__ == '__main__':
    main()
