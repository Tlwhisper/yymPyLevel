# author yym
str1 = "@扎克伯格 @明日科技 @昨日黄昏 @天使的翅膀"
list1 = str1.split(" ")
for item in list1:
    print(item[1:])  # 切片只输出好友

