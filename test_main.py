import time

time_start = time.time()
print("请输入载重重量c和古董个数n：")
c = int(input("载重重量："))
n = int(input("古董个数："))
List0 = [0]
List = List0 * n
for i in range(0, n):
    List[i] = int(input("请输入每个古董的质量："))
List.sort(reverse=False)
temp = List[0]
ans = 0
while temp <= c:
    ans = ans + 1
    temp = temp + List[ans]
print(ans)
time_end = time.time()
