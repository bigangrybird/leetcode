#!/usr/bin/python
#coding=utf8
"""
# Author: qwqian
# Created Time : 2017-12-18 23:00:16

# File Name: manacher.py
# Description:

"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = self.preprocess(s)
        n = len(s)
        center = 0
        rightbound = 0
        radius = [0 for i in range(n)]
        for i in range(1, len(s)):
            i_mirror = 2*center - i
            rightbound = radius[center] + center
            if rightbound > i:
                if radius[i_mirror] != rightbound - i:
                    radius[i] = min(radius[i_mirror], rightbound - i)
                    continue
            
            while i + radius[i] + 1 < n and i - radius[i] - 1 >= 0 and s[i + radius[i] + 1] == s[i - radius[i] - 1]:
                radius[i] += 1
                
            if radius[i] + i > rightbound:
                center = i
        
        mr = max(radius)
        indx = radius.index(mr)
        return s[indx - mr : indx + mr + 1][1::2]
                
        
        
    def preprocess(self,s):
        s2 = "#"
        for c in s:
            s2 = s2 + c + "#"
            
        return s2

def main():
    s = "babad"
    solution = Solution()
    s = solution.longestPalindrome(s)
    print s

if __name__ == "__main__":
    main()
