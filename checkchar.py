# author yym
str1 = "@名儒黄花 @天使翅膀 @人民幸福 @家国天下 @天下第一"

print(str1.count("@", 0, 7))

print("天 的index从左往右是：", str1.index("天"))
print("天 的index从右往左是：", str1.rindex("天"))

print(str1.find("@"))  # 如果不在，会抛出异常
print(str1.rfind("@"))

print("@" in str1)
try:
    print(str1.index("#"))
except ValueError:
    print("#此字符不在字符串中")

print(str1.startswith("@"))
print(str1.endswith("@"))






