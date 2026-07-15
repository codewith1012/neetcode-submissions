class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s) - 1
        score = 0
        while n > 0:
            score += abs(ord(s[n]) - ord(s[n-1]))
            n-=1;
        return score
        