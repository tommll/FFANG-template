class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Ý tưởng: Mỗi que diêm có thể được ghép vào 1 trong 4 cạnh (0/1/2/3)
        # Có N que diêm --> 4^N khả năng có thể xảy ra
        # Sử dụng backtrack để sinh ra 4^N khả năng đó

        # How to make it fast?
        # Opt 1: If we found a good configuration, return early 
        # Opt 2: Break early: if at any point current_sum[j] > ideal_length for any j, cut the branch
        # Opt 3: Sort matchsticks in descending order, so the Opt 2 condition can be met early
        # Opt 4: If we couldn't match with the i-th matchstick yet, then we would need to add some other
        # matchsticks from the remaining ones, at which the minimum we will get is current_sum[j] + matchsticks[i] + matchsticks[-1]. So, if current_sum[j] + matchsticks[i] + matchsticks[-1] > ideal_length, break

        # TC: O(4^N)
        # SC: O(logN) (sort) + O(N) (recursion stack) = O(N)

        current_sum = [0] * 4 # current_sum[i] = the current total length of the i-th side of the square
        ans = False
        matchsticks.sort(reverse=True)

        if sum(matchsticks) % 4 != 0:
            return False
        
        ideal_length = sum(matchsticks)//4

        def choose(i: int) -> None:
            """
            Choose a side for the i-th matchstick
            """
            nonlocal ans
            if i == len(matchsticks):
                if all([k == ideal_length for k in current_sum]):
                    ans = True
                return
            
            for j in range(4):
                # if current_sum[j] + matchsticks[i] <= ideal_length:
                if current_sum[j] + matchsticks[i] == ideal_length or current_sum[j] + matchsticks[i] + matchsticks[-1] <= ideal_length:
                    current_sum[j] += matchsticks[i]
                    choose(i + 1)
                    current_sum[j] -= matchsticks[i]
                if ans:
                    return
            
        choose(0)
        return ans


        # [1, 3, 6, 10]
        # ideal_length = 5
        # 

        # [10, 6, 3, 1]



