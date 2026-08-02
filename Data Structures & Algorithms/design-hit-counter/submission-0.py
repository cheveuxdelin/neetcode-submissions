# what do i see
# we can use a deque
# we dont need to individually have a unique entry for each element in the deque
# we can use a strcutre of something like [time, number_of_hits]
# if we get two consecutive hits at the same time, we can just increase the number_of_hits
# else, we do make another entry to the deque

# on getHits
# we will prune the stale characters to the left befoe
# decreasing a global varabile that is counting the total number of hits
# while this is true, and then, we just return the total

# input constraint assumptions
# the timestamps will be increasingly and in chronological order

# edge case expectations

# past 5 seconds
# [1,2,3,4,5]
# getHits on 6
# 5,4,3,2
# eviction if 6 - time_window <= 1
# its a <=

t = 0
n_hits = 1

# timestamp = 6
# time_window = 5
# [0,1],2,3,4,5,6
# to evict, 1 >= 1 

class HitCounter:
    def __init__(self):
        self.time_window = 300
        # [t, n_hits]
        self.queue = collections.deque()
        self.total_hits = 0
        
    def hit(self, timestamp: int) -> None:
        # in hitting we can just worry about writing
        # and not whats happening in the back
        if self.queue and self.queue[-1][t] == timestamp:
            self.queue[-1][n_hits] += 1
        else:
            self.queue.append([timestamp, 1])
        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        # step 1, prune stale timestamps
        while self.queue and timestamp - self.time_window >= self.queue[0][t]:
            print(self.queue, timestamp)
            self.total_hits -= self.queue.popleft()[n_hits]
        return self.total_hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
