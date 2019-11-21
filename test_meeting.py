n = int(input("请输入预约的会议总数量："))
list = [[0] * 3 for i in range(n)]

for i in range(0, n):
    list[i][0] = i + 1
    list[i][1] = int(input('请输入会议' + str(i + 1) + '的开始时间：'))
    list[i][2] = int(input('请输入会议' + str(i + 1) + '的结束时间：'))

list = sorted(list, key=lambda x: x[1], reverse=False)

print("重新排序的会议顺序如下：")
print('会议编号' + '\t' + '开始时间' + '\t' + '结束时间')
for i in range(0, len(list)):
    print(str(list[i][0]) + '\t' + str(list[i][1]) + '\t' + str(list[i][2]))
print('选择第' + str(list[0][0]) + '号会议')
sum = 1
last = list[0][2]
for i in range(1, len(list)):
    if(list[i][1] >= last):
        sum = sum + 1
        last = list[i][2]
        print('选择第' + str(list[i][0]) + '号会议')
    else:
        continue
print('一共可以安排' + str(sum) + '个会议')
