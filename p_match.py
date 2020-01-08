# author yym
import re

pattern = r"mr_\w"  # 模式串
string1 = "MR_SHOP mr_shop"  # 原串
match = re.match(pattern, string1, re.I)
print(match)
print("起始位置：", match.start())
print("结束位置：", match.end())
print("匹配结果是：", match.group())

string1 = "明日科技MR_SHOP mr_shop"  # 原串
match = re.search(pattern, string1, re.I)
print(match)
print("起始位置：", match.start())
print("结束位置：", match.end())
print("匹配结果是：", match.group())

#  findall 返回一个列表，把所有符合的都记录出来
string2 = "明日科技MR_SHOP mr_shop"  # 原串
match = re.findall(pattern, string1, re.I)
print(match)
