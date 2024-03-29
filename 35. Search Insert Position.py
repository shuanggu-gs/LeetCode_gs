# 35. Search Insert Position
# Easy
#
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        pos = -1
        if target in nums:
            pos = nums.index(target)
        else:
            for (i, n) in enumerate(nums):
                if target < n:
                    pos = i
                    break
            if pos == -1:
                pos = len(nums)

        return pos



if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    s = Solution()
    s.searchInsert(nums, target)