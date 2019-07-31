# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
    #     # write code here
    #     ll=list(matrix)
    #     matrix_new = [ll[j * cols:(j + 1) * cols] for j in range(rows)]
    #     self.rows=rows
    #     self.cols=cols
    #     # self.matirx=matrix
    #     if len(path) == 0:
    #         return False
    #     if len(matrix)==1 and matrix==path:
    #         return True
    #     ll = []
    #     for i in range(len(matrix_new)):
    #         for j in range(len(matrix_new[i])):
    #             if matrix_new[i][j] == path[0]:
    #                 ll.append([(i, j)])
    #     return self.isPath_gBpath(ll, path[1:],matrix_new)
    #
    # def isPath_gBpath(self,ll, path,matrix_new):
    #     new_path_whole = []
    #     for path_grow in ll:
    #         new_path = []
    #         if path_grow[-1][0] - 1 >= 0 and matrix_new[path_grow[-1][0] - 1][path_grow[-1][1]] == path[0]:
    #             new_path_up = path_grow[:]
    #             if (path_grow[-1][0] - 1, path_grow[-1][1]) not in new_path_up:
    #                 new_path_up.append((path_grow[-1][0] - 1, path_grow[-1][1]))
    #                 new_path.append(new_path_up)
    #         if path_grow[-1][0] + 1 <= self.rows-1 and matrix_new[path_grow[-1][0] + 1][path_grow[-1][1]] == path[0]:
    #             new_path_down = path_grow[:]
    #             if (path_grow[-1][0] + 1, path_grow[-1][1]) not in new_path_down:
    #                 new_path_down.append((path_grow[-1][0] + 1, path_grow[-1][1]))
    #                 new_path.append(new_path_down)
    #         if path_grow[-1][1] + 1 <= self.cols - 1 and matrix_new[path_grow[-1][0]][path_grow[-1][1] + 1] == path[0]:
    #             new_path_right = path_grow[:]
    #             if (path_grow[-1][0], path_grow[-1][1] + 1) not in new_path_right:
    #                 new_path_right.append((path_grow[-1][0], path_grow[-1][1] + 1))
    #                 new_path.append(new_path_right)
    #         if path_grow[-1][1] - 1 >= 0 and matrix_new[path_grow[-1][0]][path_grow[-1][1] - 1] == path[0]:
    #             new_path_left = path_grow[:]
    #             if (path_grow[-1][0], path_grow[-1][1] - 1) not in new_path_left:
    #                 new_path_left.append((path_grow[-1][0], path_grow[-1][1] - 1))
    #                 new_path.append(new_path_left)
    #         if len(new_path) != 0:
    #             for i in new_path:
    #                 new_path_whole.append(i)
    #         # else:
    #         #     new_path_whole.append(path_grow)
    #     if len(new_path_whole) == 0:
    #         return False
    #     else:
    #         if len(path) == 1:
    #             return True
    #         else:
    #             a=self.isPath_gBpath(new_path_whole, path[1:],matrix_new)
    #             return a

        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.Find(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def Find(self, matrix, rows, cols, path, i, j):
        if len(path) == 0:
            return True
        matrix[i*cols+j] = '#'
        if i - 1 >= 0 and matrix[(i - 1)*cols+j] == path[0] and self.Find(matrix, rows, cols, path[1:], i - 1, j):
            return True
        if i + 1 < rows and matrix[(i + 1)*cols+j] == path[0] and self.Find(matrix, rows, cols, path[1:], i + 1, j):
            return True
        if j - 1 >= 0 and matrix[i*cols+j - 1] == path[0] and self.Find(matrix, rows, cols, path[1:], i, j - 1):
            return True
        if j + 1 < cols and matrix[i*cols+j + 1] == path[0] and self.Find(matrix, rows, cols, path[1:], i, j + 1):
            return True
        return False

a=Solution()
# ll=list("ABCESFCSADEE")

b=a.hasPath("ABCESFCSADEE",3,4,"SEE")
print(b)