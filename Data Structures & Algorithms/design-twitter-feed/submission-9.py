import itertools

class User:
    def __init__(self):
        self.following = set()
        self.tweets = collections.deque()

class Tweet:
    def __init__(self, timestamp, id):
        self.id = id
        self.timestamp = timestamp

class Twitter:
    def __init__(self):
        self.t = itertools.count()
        self.users = defaultdict(User)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].tweets.append(Tweet(next(self.t), tweetId))
        if len(self.users[userId].tweets) > 10:
            self.users[userId].tweets.popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId].following.add(userId)
        feed = []

        for followee in self.users[userId].following:
            for tweet in self.users[followee].tweets:
                heapq.heappush(feed, (tweet.timestamp, tweet.id))
                
                if len(feed) > 10:
                    heapq.heappop(feed)
        
        feed.sort(key=lambda x: -x[0])
        return [tweet[1] for tweet in feed]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.discard(followeeId)

        
        
