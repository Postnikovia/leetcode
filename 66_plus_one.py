class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        summ = 0
        digits = digits[::-1]
        for i in range(len(digits)):
            summ += digits[i]*(10**i)
        summ+=1
        return_digits = []
        for i in str(summ):
            return_digits.append(int(i))
        return return_digits


if __name__ == "__main__":
    print(Solution().plusOne([1,2,3]))