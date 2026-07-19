class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dirt = {}

        for i in range(0, len(nums)):
            diff = target-nums[i]
            if(nums[i] in dirt):
                return [dirt[nums[i]], i]
            dirt[diff] = i
        
        print(dirt)

        return []
        