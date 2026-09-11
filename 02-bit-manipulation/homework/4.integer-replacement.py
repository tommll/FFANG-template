# https://leetcode.com/problems/integer-replacement/

# Greedy:
# When n is even, divide by half
# When n is odd,
#   If the 2nd bit is 1,
#     If all the bits are ones (11111), increase by 1 => to avoid handling the odd case for all ones (O(number of ones * 2))
#     If all the bits are ones but n = 3, decrease takes less operations (2) than increase (3). Although this is the edge case, not the norm.


class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0

        while n != 1:
            if n & 1:
                if n & (1 << 1) and n != 3:
                    n += 1
                else:
                    n -= 1
            else:
                n = n >> 1
            count += 1
        
        return count


sol = Solution()
n = 11
ans = sol.integerReplacement(n)
print(ans)
