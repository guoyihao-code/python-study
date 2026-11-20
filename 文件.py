f=open(r"C:\Users\21062\Desktop\test.txt","r",encoding="utf-8")
#print(f.read(5))#读前5个字节
#f.readlines()读取文件的所有行,并装进列表中
# contents=f.readlines()
# print(contents,type(contents))
#f.readline()只读一行，从第一行开始
#print(f.readlines())
for line in f:
    print(line)
#time.sleep()文件暂停
#文件的关闭
f.close()
#with open() as f:
