class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1

        return len(nums), nums


if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,2]))