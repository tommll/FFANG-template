class RecentCounter:
    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        if len(self.times) == 0:
            self.times.append(t)
            return 1
        else:
            idx = bisect_left(self.times, t - 3000)    
            self.times.append(t)
            if idx >= len(self.times):
                return 1
            return len(self.times) - idx


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)