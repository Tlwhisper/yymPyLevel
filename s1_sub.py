# author yym
import re
pattern = r'(黑客)|(特洛伊)'
string1 = "我是一个学生,喜欢黑客和特洛伊战争"
string2 = re.sub(pattern, "**", string1)
print("替换之前：", string1)
print("替换之后：",  string2)
