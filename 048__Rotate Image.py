class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        c=[[i]*len(matrix[0]) for i in range(len(matrix))]
        print(c)
        for j in range(len(matrix)):
            for m,i in enumerate(range(len(matrix)-1, -1, -1)):

                c[j][m]=matrix[i][j]
                print(matrix[0][0])
        return(c)


        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

a=Solution()
b=a.rotate([[1,2,3] ,[4,5,6], [7,8,9]])

print(b)

