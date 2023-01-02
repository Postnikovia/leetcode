class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


if __name__ == "__main__":
    print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))