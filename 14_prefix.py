class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        flag_prefix = True
        prefix = ""
        target_word = strs[0]
        while True:
            try:
                test_prefix = prefix + target_word[i]
            except:
                break
            for word in strs[1:]:
                if test_prefix not in word[:i+1]:
                    flag_prefix = False
                    break
            if flag_prefix:
                prefix = test_prefix
            else:
                break
            i += 1
        return prefix

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["c","acc","ccc"]))
