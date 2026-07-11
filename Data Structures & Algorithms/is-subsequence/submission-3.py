class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        refDict = {}

        for i in range(0, len(t)):
            refDict[i] = t[i]
        
        ptr=0

        for index in refDict.keys():
            if(ptr<len(s) and s[ptr] == refDict[index]):
                ptr+=1

        return ptr==len(s)