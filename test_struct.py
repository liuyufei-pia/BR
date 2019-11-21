import time

time_start = time.time()
n = int(input("请输入宝物的数量："))
m = int(input("请输入毛驴的承载能力："))
list = [[0] * 4 for i in range(n)]

for i in range(0, n):
    list[i][0] = i + 1
    list[i][1] = int((input('请输入宝物' + str(i + 1) + '的重量：')))
    list[i][2] = int(input("请输入宝物" + str(i + 1) + "的价值："))
    list[i][3] = list[i][2] / list[i][1]

list1 = sorted(list, key=lambda x: x[3], reverse=True)
sum = 0
value = 0
for i in range(0, n):
    if sum + list1[i][1] < m:
        sum = sum + list1[i][1]
        value = value + list1[i][2]
        print('装入袋子中的有宝物' + str(list1[i][0]))
    else:
        value = value + (m - sum) * list1[i][3]
        print('装入袋子中的还有一部分宝物' + str(list1[i][0]))
        print('装入袋子中的总价值为：' + str(value))
        break
