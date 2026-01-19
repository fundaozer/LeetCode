class Solution(object):
    def runningSum(self, nums):
        runningSum=[]
        k=0
        for num in nums:
            k+=num
            runningSum.append(k)
        return runningSum
                

     
        