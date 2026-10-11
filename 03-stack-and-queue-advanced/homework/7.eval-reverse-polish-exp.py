class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                item1, item2 = stack.pop(), stack.pop()
                res = 0
                match token:
                    case '+':
                        res = item1 + item2
                    case '-':
                        res = item2 - item1
                    case '*':
                        res = item1 * item2
                    case '/':
                        res = int(item2 / item1)
                stack.append(res)

        return stack[0]


# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["4","13","5","/","+"]
sol = Solution()
ans = sol.evalRPN(tokens)
print(ans)