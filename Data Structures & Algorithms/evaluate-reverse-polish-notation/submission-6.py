class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for str in tokens:
            if str == "+":
                val1 =stack.pop()
                val2 = stack.pop()
                stack.append(val1+val2)
                print(stack)
            elif str == "*":
                val1 =stack.pop()
                val2 = stack.pop()
                stack.append(val1*val2)
                print(stack)
            elif str == "-":
                val1 =stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)
                print(stack)
            elif str == "/":
                val1 =stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val1))
                print(stack)
            else:
                stack.append(int(str))
        return stack.pop()