class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for str in s:
            if str in close_to_open and len(stack)>0:
                #This means its a closing bracket
                if stack[-1] == close_to_open[str]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(str)
        if len(stack) == 0:
            return True
        return False    