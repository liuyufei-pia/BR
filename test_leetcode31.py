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
    j = 1
    temp = 0
    temp_m = 0
    n = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            temp = nums[i-1]
            n = i-1
            p = i
            temp_m = nums[i]
        else:
            if temp and (nums[i] > temp) and (nums[i]<temp_m):
                p = i
                temp_m = nums[i]
    if temp_m:
        a = nums[n]
        nums[n] = nums[p]
        nums[p] = a
    for m in range(n+1,(len(nums)-n-1)//2+n-1):   # 这儿是错误的，需要改正
        a = nums[m]
        nums[m] = nums[len(nums)-(m-n-1)-1]
        nums[len(nums)-(m-n-1)-1] = a
    print(nums)





if __name__ == '__main__':
    a = [7,6,5,4,3,2,1]
    nextPermutation(a)