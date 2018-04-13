#coding=utf-8
'''
发布包：
	1.在与包文件夹同级的路径下新建一个setup.py,在此文件中定义包的基本消息
	2.使用命令构建模块：python3 setup.py build
		能得到build目录（和包文件夹路径大致相同）
	3.使用命令打包模块：python3 setup.py sdist
		得到清单文件MANIFEST和dist目录，里面有个打包好的tar.gz包
	4.得到别人打好的包，解压，在解压目录内执行程序使用命令将打包好的模块安装到系统lib（先解压）python3 setup.py install
	5.可以不打包跳过第3步直接安装
'''
import listDir
listDir.tree.tree()
