# author yym
import re

pattern = r"mr_\w"  # 模式串
string1 = "MR_SHOP mr_shop"  # 原串
match = re.match(pattern, string1, re.I)
print(match)
print("起始位置：", match.start())
print("结束位置：", match.end())
print("匹配结果是：", match.group())
