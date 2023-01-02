class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        result_list =[]
        while True:
            if not list1:
                for k in list2:
                    result_list.append(k)
                break
            if not list2:
                for k in list1:
                    result_list.append(k)
                break
            if list1[0] <= list2[0]:
                result_list.append(list1[0])
                list1.pop(0)
            else:
                result_list.append(list2[0])
                list1.pop(0)
        return result_list


if __name__ == "__main__":
    print(Solution().mergeTwoLists(list1 = [], list2 = []))