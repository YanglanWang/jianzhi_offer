class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here

        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                break
        k = i
        for j in range(i,len(sequence)-1):
            if sequence[j]<sequence[-1]:
                return False

        # if k==len(sequence)-1:
        #     if sequence[k - 1] > sequence[-1]:
        #         return False
        #     else:
        #         return self.VerifySquenceOfBST(sequence[:k])
        # elif k==0:
        #     if sequence[-2] < sequence[-1]:
        #         return False
        #     else:
        #         return self.VerifySquenceOfBST(sequence[:-1])
        # else:
        #     if sequence[k - 1] > sequence[-1] or sequence[-2] < sequence[-1]:
        #         return False
        left=True
        right=True
        if k>0:
            left=self.VerifySquenceOfBST(sequence[:k])
        if k<len(sequence)-1:
            right=self.VerifySquenceOfBST(sequence[k:-1])

        return left and right

a=Solution()
b=a.VerifySquenceOfBST([4,6,7,5])
print(b)