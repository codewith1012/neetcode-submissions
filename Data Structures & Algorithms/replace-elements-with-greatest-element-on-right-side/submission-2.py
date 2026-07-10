class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr)==0: return []

        ptr = len(arr)-1
        grtEle = arr[ptr]
        while(ptr>=0):
            ptr -= 1
            temp = arr[ptr]
            arr[ptr] = grtEle
            grtEle = max(grtEle, temp)

        arr[len(arr)-1] = -1   
        
        
        return arr