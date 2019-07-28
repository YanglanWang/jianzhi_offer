# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        # if len(s)==0 and len(pattern)==0:
        #     return True
        # if len(s)==0:
        #     if len(pattern)==1:
        #         return False
        #     if len(pattern)>1 and pattern[1]=='*':
        #         return True
        # if len(s)!=0:
        #     if len(pattern)==0:
        #         return False
        #     if pattern[0]=='.':
        #         return self.match(s[1:],pattern[1:])
        #     if pattern[0]!='.':
        #         if pattern[0]!=s[0]:
        #             return False
        #         else:
        #             return self.match(s[1:],pattern[1:])
        # if pattern[1]=="*":
        #     if pattern[0]!='.' and pattern[0]!=s[0]:
        #         return self.match(s,pattern[2:])
        #     else:
        #         return self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)
        # else:
        #     if pattern[0]!=s[0]:
        #         return False
        #     else:
        #         if pattern[1]=='.':
        #             if len(s)<3 or len(pattern)<3:
        #                 return False
        #             else:
        #                 return self.match(s[2:],pattern[2:])
        if len(s)==0 and len(pattern)==0:
            return True
        if len(s)==1 and len(pattern)==1 and (pattern[0]==s[0] or pattern[0]=='.'):
            return True
        if len(s)>=1 and len(pattern)>1 and (pattern[0]==s[0] or pattern[0]=='.') and pattern[1]!='*':
            return self.match(s[1:],pattern[1:])
        if len(s)>=1 and len(pattern)>1 and pattern[1]=='*':
            if (pattern[0] == s[0] or pattern[0] == '.'):
                return self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)
            else:
                return self.match(s, pattern[2:])
        if len(s)==0 and len(pattern)>1 and pattern[1]=='*':
            return self.match(s,pattern[2:])

        return False

a=Solution()
b=a.match("a","ab*a")
print(b)