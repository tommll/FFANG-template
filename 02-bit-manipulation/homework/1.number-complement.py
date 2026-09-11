import math

class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(int(math.log2(num)) + 1):
            num ^= (1 << i)
        return num
