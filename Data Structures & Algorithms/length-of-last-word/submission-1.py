class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s1 = s.strip()
        for i in range(len(s1)-1,-1,-1):
            if(s1[i] == ' '): break
            count+=1
        return count