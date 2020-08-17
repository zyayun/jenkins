#!/usr/bin/env python3

#实例方法、类方法、静态方法
class testClass(object):
	#构造函数
	def	__init__(self,*args,**kwargs):
		print("构造函数",type(args))
	def say(self):
		print("instance method")
	@classmethod
	def cl1(cls):
		print("class method")
	@staticmethod
	def sta(name,age):
		print(name,age)

if __name__ == '__main__':
	print("-"*20)
   #实例方法
	a = testClass()
	a.say()
   #测试实例方法是否能调用到类方法
	a.cl1()
   #测试示例能否调用到静态方法
	a.sta('zyayun',30)
   #类方法 
	testClass.cl1()
