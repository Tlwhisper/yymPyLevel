# author yym
import re
pattern = r'(黑客)|(抓取)|(特洛伊)'
about = "我是一名程序员，喜欢看计算机网络方面的书，比如说天下第一！"
result = re.search(pattern, about)
if result is None:
    print(about, "@ 没有出现敏感字符")
else:
    print(about, "@ 出现了敏感字符！！")
