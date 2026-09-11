"""
Problem link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

Idea:

Time complexity:

Space Complexity:
"""



class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count_substr = 0
        left = 0
        count_map = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            count_map[s[right]] += 1

            while all(x >= 1 for x in count_map.values()):
                count_substr += len(s) - right
                count_map[s[left]] -= 1
                left += 1

        return count_substr

       