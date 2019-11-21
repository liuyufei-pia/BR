"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def threeSumClosest(nums, target: int):
    n = len(nums)
    if n <= 3:
        return sum(nums)
    nums.sort(reverse=False)
    res = float('inf')
    x = 0
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:    # 如果第i个数和第i-1个数相同，则跳过这个数
            continue
        left = i + 1
        right = n - 1
        while left < right:
            # 如果i、left、left+1加起来都大于target或者i、right、right-1加起来都小于target的话，计算下一个i
            if nums[i] + nums[left] + nums[left+1] > target:
                res = ok(nums[i]+ nums[left] + nums[left+1],res,target)
                return res
            if nums[i] + nums[right] + nums[right - 1] < target:
                res = ok(nums[i] + nums[right] + nums[right - 1],res,target)
                break
            temp_sum = nums[i] + nums[left] + nums[right]
            if temp_sum == target:
                return temp_sum
            res = ok(temp_sum,res, target)
            if temp_sum > target:
                right -= 1
            else:
                left += 1
            x += 1
            print(x)
    return res


def ok(a, b, c):
    if abs(a-c) < abs(b-c):
        return a
    else:
        return b


if __name__ == '__main__':
    print(threeSumClosest([1,2,4,8,16,32,64,128], 82))
