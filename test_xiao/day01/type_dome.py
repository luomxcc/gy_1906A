#
# print()在控制台打印出，type()查看变量类型
# str  a表示变量名，= 表示赋值 双引号里的数据表示值 给a赋值er
# a="er"
# print(type(a))
# print(a)
# 数字直接表示
# int是一个数字类型
# b=4
# print(type(b))
# print(b)
# []list是一个数组类型[]表示数组中间数字用逗号隔开
# c=[1,2,3,4]
# print(type(c))
# print(c)
# ()tuple表示一个元组，元组中间数字用逗号隔开
# d=(1,2,3,4)
# print(d)
# print(type(d))
# {}dict表示字典类型，中间数据用逗号给开，key和value用英文状态下冒号给开 键值对数据
# f={"姓名":"王小二","性别":"中性","联系方式":"123456"}
# print(f)
# print(type(f))
# 练习
# 第一组数据   张三,李四,王五,赵六,钱七
# 第二组数据    姓名 张三  年龄 18 性别 女  科目 语文 成绩 80
# 第三组数据   A，2,3,4,5,6,7,8,9，J,Q,K
# 第四组数据  10000
# 第五组数据  学生
# name= ["张三","李四","王五","赵六","钱七"]
# abb={"姓名":"张三","年龄":18,"性别":"女","科目":"语文","成绩":80}
# sh=["A",2,3,4,5,6,7,8,9,"J","Q","K"]
# s=10000
# m="学生"
# print(name)
# print(abb)
# print(sh)
# print(s)
# print(m)
# 小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
# q = 20
# if(q >= 20 and q > 5):
#     print(q,"小明欢天喜地的买了包大前门,拿到找零回去了！")
# if(q >= 20):
#     print(q,"小明同学买了包红双喜")
# else:
#     print(q,"小明被打出去了")
# 成人票 200 12岁以下的小孩票100 60岁以上的老人票 150 小明今年18岁，去买票应该买那种票？
# a = 18
# if(a >= 60):
#     print(a,"岁可以买到150元的老年票")
# elif(a <= 12):
#     print(a,"岁可以买到100元的儿童票")
# elif(a >= 18):
#     print(a,"你已经成年了，必须买成人票")
# elif(a < 18 and a > 12 ):
#     print(a,"没有监护人，你被暂扣了")
# else:
#     print("票已经买完了，你回去吧！")
# for i in range(100):
#  if ( i%2==1 ):
#     print(i)
#  else:
#      print("程序出错")
# for i in range(9,0,-1):
#     for j in range(1,10):
#         if j <= i:
#             print("{}*{}={}".format(i,j,i*j),end="\t")
#     print()
# # 九九乘法表
# for i in range(0,10):
#     for n in range(1,i+1):
#         print(n,"×", i ,"=" , n*i ,'\t', end='')
#     print()
# for o in range(1,10):
#     for k in range(1,o+1):
#         print(k,"+",o,"=",k+o,'\t',end='')
#     print()
#
#
# for i in range(2,100):
#     a=1#2为质数，1为合数
#     for y in range(2,i):
#         if(i%y==0):
#             a=2
#     if(a==2):
#         print(i,"合数")
#     else:
#         print(i,"质数")
#
#
