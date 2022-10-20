class Sum:
    def threeSum(self, nums: List[int]) ->List[List[int]]:
        nums = sorted(nums)
        result = set() 
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] < - nums[i]:
                    start += 1
                elif nums[start] + nums[end] > - nums[i]:
                    end -= 1
                else:
                    result.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
        return [[x[0],x[1],x[2]] for x in result]
            