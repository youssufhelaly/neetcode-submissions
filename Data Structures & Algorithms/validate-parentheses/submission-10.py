class Solution:
    def isValid(self, s: str) -> bool:
        para = {"(": ")", "{": "}", "[": "]"}

        stack = []
        for char in s:
            if char in para:
                stack.append(char)
            else:
                if not stack or char != para[stack[-1]]:
                    return False
                removed = stack.pop()

        return stack == []
