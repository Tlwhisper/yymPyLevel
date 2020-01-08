# author yym
import re
pattern = r'[?|&]'  # 只能用中括号，用小括号不好使
url = "https://www.mingrikeji?beijingshengongwuyazi&zhangwuji&hongqigong"
result = re.split(pattern, url)
print(result)
