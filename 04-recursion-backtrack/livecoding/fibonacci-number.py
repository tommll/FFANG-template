# class Solution:
#     # def __init__(self):
#     #     self.memo = {}

#     # def fib(self, n: int) -> int:
#     #     # B1: Final answer = F(n) = nth Fibonacci number
#     #     # B2: F(0) = 0, F(1) = 1
#     #     # B3: F(n) = F(n - 1) + F(n - 2)
#     #     # B4: Code
#     #     if n in self.memo:
#     #         return self.memo[n]
#     #     if n == 0 or n == 1:
#     #         return n
#     #     res = self.fib(n - 1) + self.fib(n - 2)
#     #     self.memo[n] = res
#     #     return res


#     # TC: O(1) * n = O(n)
#     # SC: O(n) (recusion stack) + O(n) (lru cache) = O(n)
#     # Đối với các bài toán đệ quy, space cần cho recursion được tính qua công thức: 
#     # Độ cao của cây đệ quy x Số lượng biến địa phương (local variable) trong hàm đệ quy
#     # n x O(1) = O(n)

#     @lru_cache(None)
#     def fib(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return n
#         return self.fib(n - 1) + self.fib(n - 2)




#     #                             F(n)
#     #             F(n - 1)                        F(n - 2)
#     #     F(n - 2)        F(n - 3)        F(n - 3)           F(n - 4)
#     # F(n - 3)    


#     # 



class Solution:
    # TC: O(log(N))
    # SC: O(log(N))
    def fib(self, n: int) -> int:
        def matmul(A, B):
            return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[1][0] + A[0][1]*B[1][1]], [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
        def matpow(A, p):
            if p == 0:
                return [[1, 0], [0, 1]]
            if p == 1:
                return A
            B = matpow(A, p >> 1)
            if p & 1:
                return matmul(matmul(B, B), A)
            return matmul(B, B)
        def fibo(n):
            A = matpow([[1, 1], [1, 0]], n - 1)
            return A[0][1]
        return fibo(n + 1)
        
