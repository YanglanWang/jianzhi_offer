class Solution:

    def printMatrix(self, matrix):

        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

    # def printMatrix(self, matrix):
    #     # write code here
    #     newList = []
    #     while matrix:
    #         newList.extend(matrix.pop(0))
    #         if matrix and matrix[0]:
    #            for row in matrix:
    #                newList.append(row.pop())
    #         if matrix:
    #             newList.extend(matrix.pop(-1)[::-1])
    #         if matrix and matrix[-1]:
    #             for row in matrix[::-1]:
    #                 newList.append(row.pop(0))
    #
    #     return newList

a=Solution()
# matrix=[range(i,i+4) for i in range(1,14,4)]
matrix=[[1],[2],[3],[4],[5]]
b=a.printMatrix(matrix)
print(b)