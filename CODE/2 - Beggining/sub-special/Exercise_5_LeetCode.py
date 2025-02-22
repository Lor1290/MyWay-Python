class Solution(object):
    def findMedianSortedArrays(nums1, nums2):
        FinalNum = nums1 + nums2
        if len(FinalNum) % 2 != 0: return FinalNum[len(FinalNum)// 2 + 1]
        else: print((FinalNum[len(FinalNum)// 2] + FinalNum[(len(FinalNum)// 2) - 1]) / 2)

Solution.findMedianSortedArrays([1, 2], [3, 4]) 