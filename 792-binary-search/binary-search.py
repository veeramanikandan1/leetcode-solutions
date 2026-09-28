class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start=0
        end=len(nums)-1
        for i in range(len(nums)):
            mid=(start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid -1
        return -1