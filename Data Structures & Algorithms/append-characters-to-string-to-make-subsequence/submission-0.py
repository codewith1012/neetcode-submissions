class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        minChars = 0

        ptr1, ptr2 = 0, 0

        while(ptr1<len(s) and ptr2<len(t)):
            if(s[ptr1] == t[ptr2]):
                ptr1+=1;
                ptr2+=1;
            else:
                ptr1+=1;

        minChars = len(t) - ptr2;

        return minChars