class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(exp):
            if exp.isdigit():
                return [int(exp)]
            ans = []
            
            for i, x in enumerate(exp):
                if x in '+-*':
                    l, r = dfs(exp[:i]), dfs(exp[i+1:])
                    
                    for x_l in l:
                        for x_r in r:
                            match x:
                                case '+':
                                    ans.append(x_l + x_r)
                                case '-':
                                    ans.append(x_l - x_r)
                                case '*':
                                    ans.append(x_l * x_r)
            
            return ans
        return dfs(expression)



        
