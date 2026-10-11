class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = []
        for x in num:
            while stack and stack[-1] > x and k > 0:
                stack.pop()
                k -= 1
            stack.append(x)

        if k > 0:
            stack = stack[:-k]

        return ''.join(stack).lstrip('0') or '0'