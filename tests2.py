
# loop : for   while

# for name  in names:
#     print(name)
#
# s = "hpojasgojadhf"
#
# for char in s:
#     print(char)

# i = 0
# # 获取list长度
# # len(x) 返回x元素的大小
# print(len(s))
# for i in range(len(s)):
#     print(i,s[i])
#
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# # list.append(x)->将x添加到list尾部
# motorcycles.append('ducati')
# print(motorcycles)
#
#
#
# # list.insert(pos,x)->将x添加到list的第pos个位置
# motorcycles.insert(0,"bwm")
# print(motorcycles)
#
# del motorcycles[0]
# print(motorcycles)
#
# # list.pop() -> 将list尾部删除
# motorcycles.pop()
# print(motorcycles)


# motorcycles.remove('yamaha')
# print(motorcycles)

# list 查找元素个数

# cnt = motorcycles.count("yamaha")
#range(x,y)->从x-> y-1  如果只有一个值
#range(y)->从0-> y-1
# for i in range(2,5):
#     print(i)
# for i in range(cnt):
#     motorcycles.remove('yamaha')
# print(motorcycles)
# while
# while "yamaha" in motorcycles:
#     motorcycles.remove("yamaha")
# print(motorcycles)

l = [3,6,4,5,1,2,7,8,9]
# motorcycles = ['honda','apple', 'yamaha', 'bwm','suzuki','yamaha']
# #排序
# # motorcycles.sort(reverse=True)
# # print(motorcycles)
#
# # reverse
#
# motorcycles.reverse()
# print(motorcycles)
l.sort()
l.reverse()
print(l)









