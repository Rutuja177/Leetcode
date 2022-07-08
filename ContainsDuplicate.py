def containsDuplicate(self, nums: List[int]) -> bool:
        list1= set(nums)
        if len(list1)==len(nums):
            return False
        else:
            return True

