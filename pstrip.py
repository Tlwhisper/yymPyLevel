# author yym
str1 = "   @www.tianxiadiyi.com.cn.#\t\n "
print(str1.strip())
print(str1)  # 不改变原来的串
print(str1.strip("\t"))
print(str1.lstrip())
print(str1.rstrip())
