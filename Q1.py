class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       nums.sort()
       for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]            
        
 #Pigeon method: here are n+1n+1 numbers and nn distinct possible numbers, the pigeonhole principle implies that if you were to put each of the n + 1n+1 pigeons into nn pigeonholes, at least one of the pigeonholes would have 2 or more pigeons.
