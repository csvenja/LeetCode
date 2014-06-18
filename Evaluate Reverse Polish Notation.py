class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        operators = ['+', '-', '*', '/']
        for item in tokens:
            if item in operators:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if item == '+':
                    stack.append(operand2 + operand1)
                elif item == '-':
                    stack.append(operand2 - operand1)
                elif item == '*':
                    stack.append(operand2 * operand1)
                else:
                    stack.append(int(float(operand2) / operand1))
            else:
                stack.append(int(item))
        return stack.pop()

#a = ["2", "1", "+", "3", "*"]
#a = ["4", "13", "5", "/", "+"]
a = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#a = ['1', '2', '+', '4', '*', '5', '+', '3', '-']

result = Solution()
print result.evalRPN(a)
