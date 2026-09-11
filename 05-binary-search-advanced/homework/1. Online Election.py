"""
Problem Link: https://leetcode.com/problems/online-election/

Idea:

Time complexity:

Space Complexity:
"""

class TopVotedCandidate:

    def __init__(self, persons, times):
        self.persons = persons
        self.times = times
        self.top = {}
        
        count = [0] * len(list(set(self.persons)))
        lead = 0
        for j, person in enumerate(self.persons):
            count[person] += 1
            if count[person] >= count[lead]:
                lead = person
            self.top[j] = lead

    def q(self, t):
        first_bigger_time_idx = bisect_right(self.times, t)
        return self.top[first_bigger_time_idx - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
