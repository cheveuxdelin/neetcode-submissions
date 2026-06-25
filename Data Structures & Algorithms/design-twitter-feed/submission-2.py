class Post:
    def __init__(self, timestamp: int, id: int):
        self.timestamp = timestamp
        self.id = id

class User:
    def __init__(self):
        self.following = set()
        self.posts = []

class Twitter:

    def __init__(self):
        self.users = defaultdict(User)
        self.n = 10
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].posts.append(Post(self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId].following.add(userId)
        feeds = [self.users[following].posts for following in self.users[userId].following]
        heap = [(-feed[-1].timestamp, feed, len(feed)-1) for feed in feeds if feed]
        heapq.heapify(heap)
        result = []
        for _ in range(self.n):
            if not heap:
                break
            _, feed, i = heapq.heappop(heap)
            result.append(feed[i].id)
            if i > 0:
                heapq.heappush(heap, (-feed[i-1].timestamp, feed, i-1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.discard(followeeId)
        
