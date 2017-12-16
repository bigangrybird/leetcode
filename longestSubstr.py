#!/usr/bin/python
#coding=utf8
"""
# Author: qwqian
# Created Time : 2017-12-16 17:39:41

# File Name: longestSubstr.py
# Description:

"""
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        maxSum = 0
        substr = []
        for char in s:
            if char in substr:
                if len(substr) > maxSum:
                    maxSum = len(substr)
                index = substr.index(char)
                substr = substr[index + 1: len(substr)]
        
            substr.append(char)
            print substr
        if len(substr) > maxSum:
            maxSum = len(substr)
        return maxSum

def main():
    s = "dvdf"
    solution = Solution()
    solution.lengthOfLongestSubstring(s)

if __name__ == "__main__":
    main()
