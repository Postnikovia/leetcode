class Solution:
    def mySqrt(self, x: int) -> int:
        answer = 0
        answer_flag = self.check_valid_answer(x, answer)
        start_ans, end_and = answer,  x
        while not answer_flag:
            answer = start_ans + (end_and-start_ans) // 2
            if answer * answer <= x:
                answer_flag = self.check_valid_answer(x, answer)
                start_ans = answer
            else:
                end_and = answer

        return answer


    @staticmethod
    def check_valid_answer(x, a):
        if (a+1)*(a+1) > x:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().mySqrt(1))