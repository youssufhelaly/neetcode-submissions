import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}
        stack = []
        res = 0
        curr = 0
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                operation = ops[token]
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append((int(operation(num2,num1))))

        return stack[-1]