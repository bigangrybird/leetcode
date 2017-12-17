#!/usr/bin/python
#coding=utf8
"""
# Author: qwqian
# Created Time : 2017-12-17 13:22:31

# File Name: medianOfTwoSortedArray.py
# Description:

"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        if n == 0:
            if m == 0:
                return None
            elif m % 2 == 1:
                return nums1[m/2]/1.0
            else:
                return (nums1[m/2-1] + nums1[m/2])/2.0

        if n == 1:
            if m % 2 == 0:
                if nums2[0] < nums1[m/2 - 1]:
                    return nums1[m/2 -1]
                elif nums2[0] < nums1[m/2]:
                    return nums2[0]
                else:
                    return nums1[m/2]
            else:
                if m == 1:
                    return (nums1[0] + nums2[0]) / 2.0
                else:
                    if nums2[0] < nums1[m/2 - 1]:
                        return (nums1[m/2 -1] + nums1[m/2]) / 2.0
                    elif nums2[0] < nums1[m/2 + 1]:
                        return (nums1[m/2] + nums2[0]) / 2.0
                    else:
                        return (nums1[m/2] + nums1[m/2 + 1]) / 2.0
        
        a = nums2[n/2]
        b = nums1[n/2]
        c = nums1[m - n/2 - 1]
        d = nums2[n/2-1]
        if m == n:
            b,c = c,b
        if a < b:
            nums2 = nums2[n/2 : n]
            nums1 = nums1[0 : m - n/2]
        elif a > c:
            if d < b:
                if n % 2 == 0:
                    nums2 = []
                else:
                    nums2 = [a]
            else:
                nums2 = nums2[0 : n - n/2]
                nums1 = nums1[n/2 : m]
        else:
            if d < b:
                nums2 = nums2[n/2 : n]
                nums1 = nums1[0 : m - n/2]
            else:
                nums1 = nums1[n/2 : m - n/2]
            
        return self.findMedianSortedArrays(nums1, nums2)

def main():
    nums1 = [1,2,3]
    nums2 = [4,5,6]
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1, nums2)
    print result

if __name__ == "__main__":
    main()
