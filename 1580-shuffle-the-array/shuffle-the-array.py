class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        arr=[]
        for i in range(n):
            left=i
            right=n+i
            a=nums[left],nums[right]
            arr.append(nums[left])
            arr.append(nums[right])
            left+=1
            right+=1
        return arr