'''
文件件操作：
close--关闭文件。相当于文件->保存
read--读取文件内容，可以把结果赋值给一个变量
readline--读取文本文件中的一行
truncate--清空文件
write(stuff)--将stuff写入文件
'''

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line1+"\n"+line2+"\n"+line3+"\n")


print("And finally, we close it.")
target.close()
