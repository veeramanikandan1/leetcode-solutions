class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findfirst():
            start=0
            end=len(nums)-1
            result=-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    result= mid
                    end=mid-1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return result
        def findlast():
            start=0
            end=len(nums)-1
            result=-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    result= mid
                    start=mid+1 
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return result
        return [findfirst(),findlast()]