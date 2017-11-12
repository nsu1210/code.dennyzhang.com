#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/find-the-difference/description/
## ,-----------
## | Given two strings s and t which consist of only lowercase letters.
## | 
## | String t is generated by random shuffling string s and then add one more letter at a random position.
## | 
## | Find the letter that was added in t.
## | 
## | Example:
## | 
## | Input:
## | s = "abcd"
## | t = "abcde"
## | 
## | Output:
## | e
## | 
## | Explanation:
## | 'e' is the letter that was added.
## `-----------
## 
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ## Idea: Use xor: xor all elements in both s and t.
        ##       We will get the character.
        ##       Here we assume the input are valid
        ## Complexity: Time: O(n), Space O(1)
        ret = 0
        for ch in s:
            ret = ret ^ ord(ch)
        for ch in t:
            ret = ret ^ ord(ch)
        return chr(ret)

    def findTheDifference1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ## Idea: 2 dicts to count the occurences of each letter
        ## Complexity: Time: O(n), Space O(n)
        small_letters = map(chr, range(ord('a'), ord('z')+1))
        s_dict = {}
        t_dict = {}
        for ch in small_letters:
            s_dict[ch] = 0
            t_dict[ch] = 0

        for ch in s:
            s_dict[ch] += 1

        for ch in t:
            t_dict[ch] += 1

        # Check status
        ch_ret = None
        has_found = False
        for ch in small_letters:
            if s_dict[ch] == t_dict[ch]:
                continue
            elif s_dict[ch] != t_dict[ch] -1:
                return None
            else:
                if has_found is True:
                    return None
                ch_ret = ch
                has_found = True

        return ch_ret
