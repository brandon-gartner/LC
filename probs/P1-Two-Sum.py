class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 4, 5, 6]
        sums = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if nums[i] in sums:
                return [sums[nums[i]], i]

            else:
                sums[needed] = i
        