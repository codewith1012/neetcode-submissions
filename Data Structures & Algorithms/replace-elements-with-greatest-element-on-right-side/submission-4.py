class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMaxEle = -1

        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = rightMaxEle
            rightMaxEle = rightMaxEle if rightMaxEle>temp else temp

        return arr
        