#Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        list1 =[]
        for i in nums:
            count = len(str(i))
            if count%2 ==0:
                list1.append(count)
        return len(list1)