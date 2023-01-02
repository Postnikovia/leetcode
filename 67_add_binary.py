class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = self.binary_to_decimal(a)
        b = self.binary_to_decimal(b)
        summ = a+b
        ret_str =""
        for i in self.decimal_to_binary(summ):
            ret_str += i
        if ret_str:
            return ret_str
        else:
            return "0"

    @staticmethod
    def binary_to_decimal(a: str) ->  int:
        summ = 0
        a = a[::-1]
        for i in range(len(a)):
            summ += int(a[i])*(2**i)
        return summ

    @staticmethod
    def decimal_to_binary(a: int)-> str:
        binar_digts_list = []
        while a != 0:
            binar_digts_list.append(str(a%2))
            a = a//2

        return binar_digts_list[::-1]

if __name__ == "__main__":
    print(Solution().addBinary("0","0"))
