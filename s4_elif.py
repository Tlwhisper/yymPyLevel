# author yym
# 嵌套分支
print("将会判定您是否酒驾车")
num = int(input("请输入酒精含量百分比："))
if num < 20:
    print("健康驾车！！！")
elif num > 20:
    if num <= 30:
        print("1级饮酒驾车！")
    elif num < 40:
        print("2级饮酒驾车！！")
    elif num < 50:
        print("3级饮酒驾车！！！")
    elif num < 60:
        print("4级饮酒驾车！！！！")
    else:
        print("5级饮酒驾车！！！！")
else:
    print("20特别危险！！！")

