class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [] , []
        for i,par in enumerate(s):
            if par == '(':
                left.append(i)
            if par == '*':
                star.append(i)
            if par == ')':
                if len(left)>0:
                    left.pop()
                elif len(star)>0:
                    star.pop()
                else:
                    return False
        while left and star:
            if left.pop()>star.pop():
                return False
        return not left