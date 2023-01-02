class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        tmp_counter = 0
        for i in s:
            if i == " ":
                if tmp_counter:
                    counter = tmp_counter
                tmp_counter = 0
            else:
                tmp_counter += 1
        if tmp_counter:
            return tmp_counter
        else:
            return counter


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))

