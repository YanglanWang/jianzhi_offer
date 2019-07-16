# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        fenhao = 0
        # if s[0] == '+' or s[0] == '-':
        #     s = s[1:]
        for i in range(len(s)):
            if s[i] == 'e' or s[i]=='E':
                if len(s[i+1:])==0:
                    return False
                result = (self.isInt(s[0:i]) or self.isFloat(s[0:i])) and (
                            self.isInt(s[i + 1:]) )
                return result
            elif s[i] >= '0' or s[i] <= '9' or i == '.':
                pass
            else:
                return False
        result = (self.isInt(s) or self.isFloat(s))
        return result

    def isInt(self, s):
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        for i in s:
            if i >= '0' and i <= '9':
                pass
            else:
                return False
        return True

    def isFloat(self, s):
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        dianshu = 0
        for i in s:
            if i >= '0' and i <= '9':
                pass
            elif i == '.' and dianshu == 0:
                dianshu+=1
                pass
            else:
                return False
        return True


a=Solution()
b=a.isNumeric("12e+5.4")
print(b)