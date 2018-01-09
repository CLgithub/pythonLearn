#coding=utf-8
'''
文件(夹)的增删改名查操作
    改变默认路径
        获取当前操作路径：os.getcwd()
        改变当前操作路径：os.chdir("../")
    文件：
        增 不需要导入os，直接f=open("filePath","w+")，记得要关闭
	删 导入os，os.remove("filePath")，删除filePaht对应的文件
	改 更改文件内容，不需要导入os，直接open("filePaht","w+")，更改文件名,导入os,os.rename("oldfilePath","newFilePaht")
	查 查看文件内容，不需要导入os，直接f=open("filePath","r+"),查看文件列表,导入os,fileList=os.listdir("./") 得到当前路径下所有文件及文件夹名称，并以列表形式返回

    文件夹:
        增 导入os,os.mkdir("dirPath") 
	删 导入os,os.rmdir("dirPath")
	改 与文件一样，os.rename("old","new")
	查 与文件一样，os.listdir("./")
'''
import os #导入os相关包，
print("os.getcwd()=%s"%os.getcwd())
os.chdir("../")
print("os.getcwd()=%s"%os.getcwd())
os.chdir("./day8")
print("os.getcwd()=%s"%os.getcwd())
#文件
#增
f=open("file2","w+")
f.write("abcdefg")
f.close()
#改
os.rename("file2","../file2_2")
#查
listFile=os.listdir("../")
print("ls../=%s"%listFile)
#删
os.remove("../file2_2")

#文件夹
#增
os.mkdir("./dir1")
#改 与文件操作方式相同
os.rename("dir1","../dir2")
#查 与文件操作方式相同
#删
os.rmdir("../dir2")
