#time Complexity:O(N^N)
#leetcode submission:successful
#we use backtracking to solve
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
       
        
        self.helper(result,candidates,target,[],0)
        return result
    def helper(self,result,candidates,target,temp,index):
            
            if target<0:
                return
            if target==0:
                result.append(temp[:])
                return
            for i in range(index,len(candidates)):
                if candidates[i]<=target:
                    

                    temp.append(candidates[i])
                    self.helper(result,candidates,target-candidates[i],temp,i)
                    temp.pop()    