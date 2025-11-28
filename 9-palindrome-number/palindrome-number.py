class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            real_x=x
            y=0
            while x>0:
                y=y*10+x%10
                x//=10
            return real_x==y

            
        