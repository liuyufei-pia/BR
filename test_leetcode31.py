"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def nextPermutation(nums: list):
    first = -1
    n = len(nums)

    # 定义排序函数，后边用得到
    def reverse(nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    # 找到第一个i小于i+1的数
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            first = i
            break
    # 如果没找到，倒序
    if first == -1:
        reverse(nums, 0, n - 1)
        return
    second = -1
    # 找到第一个比num[first]大的数nums【second】
    for i in range(n - 1, first, -1):
        if nums[i] > nums[first]:
            second = i
            break
    nums[first], nums[second] = nums[second], nums[first]
    reverse(nums, first + 1, n - 1)
    print(nums)


if __name__ == '__main__':
    a = [1,2,8,7,6,5,4,3,1]
    nextPermutation(a)