class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = [*str(x)]
        x_reverse = x.copy()
        x_reverse.reverse()
        
        return x == x_reverse


run = Solution()
run.isPalindrome(121)
run.isPalindrome(1)
run.isPalindrome(10)
