class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        List=[]
        while matrix and matrix[0]:

            if matrix and matrix[0]:
                List.extend(matrix.pop(0))

            if matrix and matrix[0]:
                print(matrix)
                for row in matrix:
                    print(1)
                    c=row.pop()
                    List.append(c)
            if matrix and matrix[0]:
                List.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    c=row.pop(0)
                    List.append(c)
        #print(List)
        return(List)

matrix=[[3], [2]]
a=Solution()
b=a.spiralOrder(matrix)
print(b)



