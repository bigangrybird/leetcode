#!/usr/bin/python
#coding=utf8
"""
# Author: qwqian
# Created Time : 2017-12-20 22:56:33

# File Name: zigzagConversion.py
# Description:

"""
class Solution(object):
    def covert(self, s, numRows):
        if numRows == 1 or len(s) < numRows:
            return s

        l = ['']*numRows
        index, step = 0, 1
        for char in s:
            l[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(l)
