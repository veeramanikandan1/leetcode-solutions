class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m=sorted(nums1+nums2)
        start=0
        end=len(m)-1
        mid = (start+end)//2
        if len(m)%2!=0:
            return m[mid] 
        else:
            ans=(m[mid+1]+m[mid])/2
            return ans