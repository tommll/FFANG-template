class Solution:
    def myPow(self, x: float, n: int) -> float:
        # B1: F(n) = x^n 
        # B2: Base case: F(0) = 1
        # B3: if n < 0, F(n) = 1.0/F(-n)
        # if n > 0, if n = 2k, F(n) = F(n//2) * F(n//2), otherwise F(n) = F(n//2) * F(n//2) * x

        # TC: O(n)
        # SC: 

        def F(n: int) -> float:
            """Return x^n"""
            if n == 0:
                return 1
            if n < 0:
                return 1.0 / F(-n)
            half = F(n // 2)
            if n & 1:
                return half * half * x
            return half * half

        return F(n)

        # TC: O(log_2(N)) = O(log(N))
        # SC: O(1) * log_2(N) = O(log(N))

        # n --> n/2 --> n/4 --> n/8 --> ... --> 1 --> 0
        # Số bước của dãy trên: log_2(N) +- 1
        # Tại sao là log_2(N)? 
        # Gọi số bước là X, thì 2^X = N --> X = log_2(N)


