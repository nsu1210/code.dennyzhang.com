
# Leetcode: Flipping an Image     :BLOG:Basic:

---

Flipping an Image  

---

Similar Problems:  

-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.  

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].  

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].  

Example 1:  

    Input: [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]
    Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:  

    Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
    Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Notes:  

-   Width and height of A are in between 1 and 20
-   0 <= A[i][j] <= 1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/flipping-an-image)  

Credits To: [leetcode.com](https://leetcode.com/problems/flipping-an-image/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/flipping-an-image
    // Basic Ideas: One pass, two-pointers
    // Complexity: Time O(m*n), Space O(1)
    func flipAndInvertImage(A [][]int) [][]int {
        for i, row := range A {
    	for l,r := 0,len(row)-1; l<=r; l,r=l+1,r-1 {
    	    A[i][l], A[i][r] = 1-A[i][r], 1-A[i][l]
    	}
        }
        return A
    }
