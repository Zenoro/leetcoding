class Solution(object):
    def maxNumberOfBalloons(self, text):
        s = set("balloon")
        dd = {k:0 for k in s}
        for char in text:
            if char in s:
                dd[char] += 1
        dd['l'] //= 2
        dd['o'] //= 2
        return min(dd.values())


print(Solution().maxNumberOfBalloons("nlaebolko"))
print(Solution().maxNumberOfBalloons("leetcode"))
print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
