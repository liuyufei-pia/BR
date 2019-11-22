"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。
示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def foursum(nums:list, target:int) -> list:
    n = len(nums)
    if n <= 3:
        return []
    elif n == 4:
        if sum(nums) == target:
            return [nums]
        else:
            return []
    nums.sort(reverse=False)
    ans_temp = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(n-1,0,-1):
            if j < n-1 and nums[j] == nums[j + 1]:
                continue
            left = i+1
            right = j-1
            if nums[i] > target and target >=0:
                return ans_temp
            while left < right:
                sum_temp = nums[i] + nums[left] + nums[right] + nums[j]
                if sum_temp == target:
                    ans_temp.append([nums[i],nums[left],nums[right],nums[j]])
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    right -= 1
                    left += 1
                if sum_temp > target:
                    right -= 1
                if sum_temp < target:
                    left += 1
    return ans_temp


if __name__ == '__main__':
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11
    a = foursum(nums,target)
    print(a)
