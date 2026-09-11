"""
Problem link: https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

Idea:

Time complexity:

Space Complexity:
"""


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tails, ans = [], []
        for obs in obstacles:
            idx = bisect_right(tails, obs)
            if idx == len(tails):
                tails.append(obs)
            else:
                tails[idx] = obs   # replace, don't truncate
            ans.append(idx + 1)
        return ans

