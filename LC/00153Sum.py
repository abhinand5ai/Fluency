class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
      nums.sort()
      n = len(nums)
      print(nums)
      res = []
      for i in range(n):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
          if nums[j] + nums[k] < -nums[i]:
            j += 1
          elif nums[j] + nums[k] == -nums[i]:
            res.append((nums[i],nums[j],nums[k]))
            j += 1
            k -= 1
            while j < k and nums[j] == nums[j - 1]:
                j += 1
                
          else:
            k -= 1
        
      return res
      
            
        