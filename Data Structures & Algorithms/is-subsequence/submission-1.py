class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1, ptr2 = 0, 0

        if(len(s) > len(t)): return False
        
        while(ptr1<len(s) and ptr2<len(t)):
            if(s[ptr1] == t[ptr2]):
                ptr1+=1
                ptr2+=1
                continue
            ptr2+=1
        

        return ptr1==len(s)