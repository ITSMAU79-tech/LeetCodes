class Solution:
    def leftRightDifference(self, nums):
        total = sum(nums)
        left = 0
        answer = []

        for i in range(len(nums)):
            right = total - left - nums[i]
            answer.append(abs(left - right))
            left += nums[i]

        return answer