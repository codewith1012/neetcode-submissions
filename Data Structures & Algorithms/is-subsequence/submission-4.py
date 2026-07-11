class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr=0

        for index in range(0, len(t)):
            if(ptr<len(s) and s[ptr] == t[index]):
                ptr+=1

        return ptr==len(s)