from typing import List


nums = [3,5,0,5,8,10,15,74,88,4]
target = 9

def twoSum(nums: List[int], target: int) -> List[int]:
    indices = []
    diff_dict = {}
    for idx in range(len(nums)):
        value = nums[idx]
        # check if any such number is there in diff_dict such that value + number = target
        diff = target - value
        if diff in diff_dict.keys():
            indices.extend([diff_dict[diff] ,idx])
            break
        else:
            diff_dict.update({value :idx})
    return indices

print(twoSum(nums,target))