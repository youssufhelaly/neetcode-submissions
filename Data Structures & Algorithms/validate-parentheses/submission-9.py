class Solution:
    def isValid(self, s: str) -> bool:
        para = {'(':')', '{':'}','[':']'}

        stack = []
        for char in s:
            if char in para:
                stack.append(char)
            else:
                if not stack:
                    return False
                removed = stack.pop()
                if char != para[removed]:
                    return False
        return stack == []
