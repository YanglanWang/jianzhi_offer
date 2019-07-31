# class Solution:
#     path_complete = []
#     dict_n={}
#     def movingCount(self, threshold, rows, cols):
#         # write code here
#         self.threshold = threshold
#         self.rows = rows
#         self.cols = cols
#         path = [[(0, 0)]]
#         self.dict_n[(0,0)]=1
#         self.GeneratePath(path)
#         return len(self.dict_n)
#
#
#     def GeneratePath(self, path):
#         path_uncomplete = []
#         for path_tmp in path:
#             path_new = []
#             if path_tmp[-1][0] - 1 >= 0 and self.judge((path_tmp[-1][0] - 1, path_tmp[-1][1])) == True:
#                 path_tmp_up = path_tmp[:]
#                 if (path_tmp[-1][0] - 1, path_tmp[-1][1]) not in path_tmp_up and (path_tmp[-1][0] - 1, path_tmp[-1][1]) not in self.dict_n:
#                     self.dict_n[(path_tmp[-1][0] - 1, path_tmp[-1][1])]=1
#                     path_tmp_up.append((path_tmp[-1][0] - 1, path_tmp[-1][1]))
#                     path_new.append(path_tmp_up)
#             if path_tmp[-1][0] + 1 <= self.rows - 1 and self.judge((path_tmp[-1][0] + 1, path_tmp[-1][1])) == True:
#                 path_tmp_down = path_tmp[:]
#                 if (path_tmp[-1][0] + 1, path_tmp[-1][1]) not in path_tmp_down and (path_tmp[-1][0] + 1, path_tmp[-1][1]) not in self.dict_n:
#                     self.dict_n[(path_tmp[-1][0] + 1, path_tmp[-1][1])]=1
#                     path_tmp_down.append((path_tmp[-1][0] + 1, path_tmp[-1][1]))
#                     path_new.append(path_tmp_down)
#             if path_tmp[-1][1] + 1 <= self.cols - 1 and self.judge((path_tmp[-1][0], path_tmp[-1][1] + 1)) == True:
#                 path_tmp_right = path_tmp[:]
#                 if (path_tmp[-1][0], path_tmp[-1][1] + 1) not in path_tmp_right and (path_tmp[-1][0], path_tmp[-1][1] + 1) not in self.dict_n:
#                     self.dict_n[(path_tmp[-1][0], path_tmp[-1][1] + 1)]=1
#                     path_tmp_right.append((path_tmp[-1][0], path_tmp[-1][1] + 1))
#                     path_new.append(path_tmp_right)
#             if path_tmp[-1][1] - 1 >= 0 and self.judge((path_tmp[-1][0], path_tmp[-1][1] - 1)) == True:
#                 path_tmp_left = path_tmp[:]
#                 if (path_tmp[-1][0], path_tmp[-1][1] - 1) not in path_tmp_left and (path_tmp[-1][0], path_tmp[-1][1] - 1) not in self.dict_n:
#                     self.dict_n[(path_tmp[-1][0], path_tmp[-1][1] - 1)]=1
#                     path_tmp_left.append((path_tmp[-1][0], path_tmp[-1][1] - 1))
#                     path_new.append(path_tmp_left)
#             if len(path_new) == 0:
#                 self.path_complete.extend(path_tmp)
#             else:
#                 path_uncomplete.extend(path_new)
#         while len(path_uncomplete) != 0:
#             self.GeneratePath(path_uncomplete)
#         if len(path_uncomplete)==0:
#             return
#
#     def toNumDigit(self, number):
#         num_array = map(int, (str(number)))
#         return sum(num_array)
#
#
#
#     def judge(self, (row_tmp, col_tmp)):
#         sum = self.toNumDigit(row_tmp) + self.toNumDigit(col_tmp)
#         if sum <= self.threshold:
#             return True
#         else:
#             return False
class Solution:

    # def __init__(self):
    #     self.vis = {}
    #
    # def movingCount(self, threshold, rows, cols):
    #     # write code here
    #     return self.moving(threshold, rows, cols, 0, 0)
    #
    # def moving(self, threshold, rows, cols, row, col):
    #     if row / 10 + row % 10 + col / 10 + col % 10 > threshold:
    #         return 0
    #     if row >= rows or col >= cols or row < 0 or col < 0:
    #         return 0
    #     if (row, col) in self.vis:
    #         return 0
    #     self.vis[(row, col)] = 1
    #
    #     return 1 + self.moving(threshold, rows, cols, row - 1, col) + self.moving(threshold, rows, cols, row + 1,
    #                                                                               col) + self.moving(threshold, rows,
    #                                                                                                  cols, row,
    #                                                                                                  col - 1) + self.moving(
    #         threshold, rows, cols, row, col + 1)

    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        self.Count(threshold, rows, cols, matrix, 0, 0)
        sum=0
        for i in matrix:
            for j in i:
                sum+=int(j)
        return sum
    def Count(self, threshold, rows, cols, matrix, i, j):
        list_i =[int(a) for a in list(str(i))]
        list_j=[int(b) for b in list(str(j))]

        if sum(list_i) + sum(list_j) <= threshold:
            matrix[i][j] = 1
            if i - 1 >= 0 and matrix[i - 1][j] == 0 :
                self.Count(threshold, rows, cols, matrix, i - 1, j)
            if i + 1 < rows and matrix[i + 1][j]==0:
                self.Count(threshold, rows, cols, matrix, i + 1, j)
            if j - 1 >= 0 and matrix[i][j - 1]==0:
                self.Count(threshold, rows, cols, matrix, i, j - 1)
            if j + 1 < cols and matrix[i][j + 1]==0:
                self.Count(threshold, rows, cols, matrix, i, j + 1)



a=Solution()
b=a.movingCount(5,10,10)
print(b)