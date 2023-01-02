class Solution:
    brackets_dict = {"}" : "{", "]": "[", ")": "("}
    def isValid(self, s: str) -> bool:
        brackets_stak = []
        for i in s:
            if i in self.brackets_dict.values():
                brackets_stak.append(i)
            else:
                if not brackets_stak:
                    return False
                if self.brackets_dict[i] == brackets_stak[-1]:
                    brackets_stak.pop(-1)
                else:
                    return False

        if brackets_stak:
            return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().isValid("(]"))