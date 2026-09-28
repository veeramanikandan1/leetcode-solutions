class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            r= nums[nums[i]]
            a.append(r)
        return a