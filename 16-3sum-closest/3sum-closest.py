class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)): 
            left=i+1
            right=len(nums)-1
            
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if abs(total-target)<abs(close-target):
                    close=total
                if total==target:
                    return total 
                elif target<total:
                    right-=1
                elif target>total:
                    left+=1
        return close
                
