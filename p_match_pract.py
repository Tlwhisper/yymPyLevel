# author yym
import re

pattern = r'(13[4-9]\d{8})|(15[01289]\d{8})'
mobile = "13644443333"
match1 = re.match(pattern, mobile)
if match1 is None:
    print(mobile, "不是一个有效的移动手机号码")
else:
    print(mobile, "是一个有效的移动手机号码")
