"""
Problem Link: https://leetcode.com/problems/k-closest-points-to-origin/description/

Idea:

Time complexity:

Space Complexity:
"""

from math import sqrt, pow
import random

class Solution:
    def __init__(self):
        self.ans = []

    def kClosest(self, arr, d):
        def computeDis(point):
            return sqrt(pow(point[0], 2) + pow(point[1], 2))
        def compare(x, y):
            xDis, yDis = computeDis(x), computeDis(y)
            if xDis < yDis: return -1
            if xDis > yDis: return 1
            return 0

        def pick(points, k):
            pivot = random.choice(points)
            less = [x for x in points if compare(x, pivot) == -1]
            equal = [x for x in points if compare(x, pivot) == 0]

            if k < len(less):
                self.kClosest(less, k)
                return
            if k == len(less):
                self.ans += less
                return
            if k <= len(less) + len(equal):
                self.ans += less + equal[:(k-len(less))]
                return
            self.ans += less + equal
            self.kClosest([x for x in points if compare(x, pivot) == 1], k - len(less) - len(equal))


        pick(arr, d)
        return self.ans

