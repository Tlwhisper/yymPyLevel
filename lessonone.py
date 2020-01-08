# # author yym
# tid = input("请输入一段文字\n")
# print(tid)
# # 截取字符串
str1 = "引刀成一快，不负少年头"
print(str1[0:5])
print(str1[0:11:2])
print(str1[19:])  # 使用切片截取不会抛出异常，使用索引会抛出异常
# print(str1[19])
try:
    print(str1[18])
except IndexError:
    print("索引不存在！！！")





