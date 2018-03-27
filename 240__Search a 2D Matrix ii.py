class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        n = len(matrix)  # row
        m = len(matrix[0])  # column
        for j in range(m):
            for i in range(n):
                if matrix[i][j] < target:
                    continue
                elif matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
        return False

    def searchMatrix2(self, matrix, target):
        if not matrix:
            return False
        if not matrix[0]:
            return False
        n = len(matrix)  # row
        m = len(matrix[0])  # column
        List = []
        for i in range(n):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                List.append(i)
        Xist = []
        for i in range(m):
            if target >= matrix[0][i] and target <= matrix[-1][i]:
                Xist.append(i)
        for p in List:
            for q in Xist:
                if matrix[p][q] == target:
                    return True
        return False

    def searchMatrix3(self,matrix,target):
        if not matrix:
            return False
        rows = len(matrix)  # row
        cols = len(matrix[0])  # column
        i = 0
        j = cols-1
        while i<rows and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j=j-1
                #列首直接大于TARGET
                #往前缩一列
            elif matrix[i][j] <target:
                i+=1
                #行尾直接小于Target
                #往下加一行
        return False

    #91ms
