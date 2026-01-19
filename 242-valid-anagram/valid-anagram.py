class Solution(object):
    def isAnagram(self, s, t):
        x=tuple(sorted(s))
        y=tuple(sorted(t))
        if x==y :
            return True
        else :
            return False
       
        