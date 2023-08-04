"""
Plan
news feed - queue 
postTweet: appendleft to queue (userId, tweetId)
getNewsFeed: iterate over queue, if tweet userId == currentUserId OR tweet userId in hashmap (max 10)
follow (add) / unfollow (remove) - hashmap (followerId : set(followeeIds))
"""

from collections import defaultdict, deque

class Twitter:
    
    def __init__(self):
        self.followerHashMap = defaultdict(set)
        self.timeline = deque()

    # O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timeline.appendleft((userId, tweetId))

    # ~O(n), n = number of tweets in timeline (assuming user or followee's tweets were made at the beginning)  
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i = 0
        while len(res) < 10 and i < len(self.timeline):
            if userId == self.timeline[i][0] or self.timeline[i][0] in self.followerHashMap[userId]:
                res.append(self.timeline[i][1])
            i += 1
        return res
    
    # O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerHashMap[followerId].add(followeeId)
        
    # O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerHashMap[followerId]:
            self.followerHashMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)