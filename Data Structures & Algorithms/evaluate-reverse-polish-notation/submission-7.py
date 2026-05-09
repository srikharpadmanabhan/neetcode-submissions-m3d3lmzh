class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operands = ['+', '-', '*', '/']

        def apply_operand(operand, a, b):
            if operand == '+':
                return a + b
            elif operand == '-':
                return a - b
            elif operand == '*':
                return a * b
            elif operand == '/':
                return int(a / b)
            else:
                return 0

        for token in tokens:
            print(stack)
            if token not in operands:
                stack.append(int(token))
            else:
                print(token)
                second = stack[-1]
                first = stack[-2]

                stack = stack[:-2]

                stack.append(apply_operand(token, first, second))
        
        return stack[-1]
