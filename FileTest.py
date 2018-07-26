# 文件操作  open write read  close

#默认为只读 r
# nameFile = open("name.txt","w")
# nameFile.write("张三")
#
# nameFile.close()


#nameFile = open("name.txt","a") 在文件后追加
# nameFile = open("name.txt","w")
# nameFile.write("lisi")
# nameFile.write("\n") # 换行
# nameFile.write("wangwu")
#
#
# nameFile.close()


# nameFile = open("name.txt")
# names = nameFile.readlines()
#
# for name in names:
#     print(name)
#     print("============")
#
# print("dddddddddd")
#
#
# nameFile.close()



file6 = open('name.txt')
print('当前文件指针的位置 %s' %file6.tell())
print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
# 第一个参数代表偏移位置，第二个参数  0 表示从文件开头偏移  1表示从当前位置偏移，   2 从文件结尾
file6.seek(5,0)
print('我们进行了seek操作')
print('当前文件指针的位置 %s' %file6.tell())
print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
file6.close()









