class Solution(object):
    def romanToInt(self, s):
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev=0
        sum=0
        for ch in s[::-1]:
            value=roman[ch]
            if value<prev:
                sum-=value
            else:
                sum+=value
            prev=value
        return sum



        