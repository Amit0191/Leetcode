'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

'''

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum = [self.nums[0]]
        for i in range(1, len(self.nums)):
            prefix_sum.append(prefix_sum[i-1] + self.nums[i])
        if left == 0:
            return prefix_sum[right]
        return prefix_sum[right] - prefix_sum[left-1]
