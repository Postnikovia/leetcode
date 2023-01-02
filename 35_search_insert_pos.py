class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if target <= nums[i]:
                return i
            i += 1
        return len(nums)


if __name__ == "__main__":
    print(Solution().searchInsert(nums = [1], target = 0))