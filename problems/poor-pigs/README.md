
# Leetcode: Poor Pigs     :BLOG:Hard:

---

Identity the poison bucket with mininum pigs  

---

Similar Problems:  

-   [Review: Math Problems,](https://code.dennyzhang.com/review-math) Tag: [math](https://code.dennyzhang.com/tag/math)

---

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.  

Answer this question, and write an algorithm for the follow-up general case.  

Follow-up:  

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/poor-pigs)  

Credits To: [leetcode.com](https://leetcode.com/problems/poor-pigs/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/poor-pigs
    class Solution(object):
        def poorPigs(self, buckets, minutesToDie, minutesToTest):
    	"""
    	:type buckets: int
    	:type minutesToDie: int
    	:type minutesToTest: int
    	:rtype: int
    	"""
