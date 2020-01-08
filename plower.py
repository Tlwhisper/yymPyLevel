# author yym
user_name = "|Wangming|xiAohong|XIAOhua|YANGyanmeng|LINGfucong"
user_name1 = user_name.lower()
re_name = input("请输入你的用户名：")
re_name2 = "|" + re_name.lower() + "|"
if re_name2 in user_name1:
    print(re_name2 + "此用户名已经存在！！！")
else:
    print("good name ! !")



