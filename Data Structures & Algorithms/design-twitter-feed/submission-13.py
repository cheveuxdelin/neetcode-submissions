# at most 10. means, if there are total tweets less than 10, you give less
# we include same user posts within these last 10 posts

# to avoid duplicate follows and following we can use a in-memory set
# but in a real production this does not approach real scenario
# so ill assume all calls to folowing/unfollowing are valid

# the key of this problem is that, if we keep ordered each user posts array
# the problem reduces to be a k-way merge!


class User:
    def __init__(self):
        self.following = set()
        self.posts = []        
    
class Tweet:
    def __init__(self, tweet_id: int, timestamp: int):
        self.tweet_id = tweet_id
        self.timestamp = timestamp
    
    def __lt__(self, other):
        return self.timestamp > other.timestamp

t = 0

def get_timestamp():
    global t
    t += 1
    return t


class Twitter:
    def __init__(self):
        # [id_of_user, user]
        self.users = collections.defaultdict(lambda: User())

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].posts.append(Tweet(tweetId, get_timestamp()))        

    def getNewsFeed(self, userId: int) -> List[int]:
        relevant_user_ids = self.users[userId].following | set([userId])

        heap = []
        for user_id in relevant_user_ids:
            stream = reversed(self.users[user_id].posts)
            first_tweet = next(stream, None)
            if first_tweet:
                heapq.heappush(heap, (first_tweet, stream))

        result = []
        while heap and len(result) < 10:
            tweet, stream = heapq.heappop(heap)
            result.append(tweet.tweet_id)

            # check for next
            next_tweet = next(stream, None)
            if next_tweet:
                heapq.heappush(heap, (next_tweet, stream))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.discard(followeeId)
        
