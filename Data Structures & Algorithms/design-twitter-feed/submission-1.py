class Twitter:

    def __init__(self):
        self.time = 0
        self.usersTweetsMap = defaultdict(list)
        self.usersFolloweeMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None: 
        self.usersTweetsMap[userId].append((self.time,tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]: 
        maxHeap = []
        self.usersFolloweeMap[userId].add(userId)
        for followee in self.usersFolloweeMap[userId]:
            followeeTweets = self.usersTweetsMap[followee]
            iterations = min(10, len(followeeTweets))
            for i in range(iterations):
                heapq.heappush(maxHeap, followeeTweets[-(i + 1)])      
        ans = []
        while maxHeap and len(ans) < 10:
            ans.append(heapq.heappop(maxHeap)[1]) 
        return ans

    def follow(self, followerId: int, followeeId: int) -> None: 
        self.usersFolloweeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: 
        if followerId != followeeId and followeeId in self.usersFolloweeMap[followerId]:
            self.usersFolloweeMap[followerId].remove(followeeId)
        
