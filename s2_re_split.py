# author yym
import re

pattern = r'[?|&]'  # 只能用中括号，用小括号不好使
url = "https://www.mingrikeji?beijingshengongwuyazi&zhangwuji&hongqigong"
result = re.split(pattern, url)
print(result)

# 把艾特的好友都表示出来
pattern = r'\s*@'  # \s表示空字符  *表示限定符
list1 = "@明日科技 @令狐葱 @神雕侠 @小龙女 @无崖子"
result = re.split(pattern, list1)
print("您的好友如下：")
for item in result:
    if item != "":
        print(item)

