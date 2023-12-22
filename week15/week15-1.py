class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ans = 0
        for left in range(n-1):
            now = 0
            for i in range(n):
                if i<=left and s[i]=='0':now +=1
                if i>left and s[i]=="1":now +=1
            if now > ans: ans=now
        return ans
#########################################################################
class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0

        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            ans = max(ans, left.count('0') + right.count('1'))

        return ans