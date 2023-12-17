class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.time = timeToLive
        self.token = defaultdict(int)
        
    def generate(self, tokenId, currentTime):
        self.token[tokenId] = currentTime + self.time

    def renew(self, tokenId, currentTime):
        if self.token[tokenId] > currentTime:
            self.token[tokenId] = currentTime + self.time

    def countUnexpiredTokens(self, currentTime):
        count = 0
        for i in self.token.keys():
            if self.token[i] > currentTime:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)