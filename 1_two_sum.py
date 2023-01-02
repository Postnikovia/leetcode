class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index_one in range(len(nums)):
            index_two = self.find_number_in_array(nums, index_one+1, target-nums[index_one])
            if index_two:
                return [index_one, index_two]

    @staticmethod
    def find_number_in_array(nums: list[int], start_index: int, number: int):
        for i in range(start_index, len(nums)):
            if nums[i] == number:
                return i

 
if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
