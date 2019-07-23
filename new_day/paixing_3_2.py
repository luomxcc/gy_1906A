# def pukepai_3_2(a):
#     # a = input("shur ")
#     a =a.replace('"',"''")
#     # print(a)
#     # 第二步：去掉中括号 字符串截取  [::]
#     a = a[3:-3]
#     # print(a)
#     # 第三步：变成list  字符串切片  .split（） 新建一个list变量
#     b = a.split("'' , ''")
#     # print(b)
#     # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
#     k = {}
#     for s in b :
#         x = s[1:]
#         # print(x)
#     # 第五步：统计相同的数字个数  用字典去统计
#         if(x in k ):
#             k[x] +=1
#         else:
#             k[x] = 1
#     # print(k)
#     # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
#     # 如果key对应的数值有3的 v1 = 1，如果没有则为0
#     # 如果key对应的数值有2的 v2 = 1，如果没有则为0
#     v1 = 0
#     v2 = 0
#     for key in k:
#         if(k[key] == 3):
#             v1 = 1
#         if(k[key] == 2):
#             v2 = 1
#     if(v1 == 1 and v2 == 1):
#         print("三带二，收钱")
#     else:
#         print("要不起，走开")
#
# # for i in range(3):
#     # pukepai_3_2()
# with open("D:\\software\\pycharm\\luomingxing_2019-07-17\\new_day\\paixing.txt","r") as q :
#     y = q.readlines()
#     # print(y)
#     for b in y:
#         le =b.replace ("\n","")
#         # print(le)
#         pukepai_3_2(le)
#         # print(le)
# print("跨进水果店")
# jiage = 4
# print("导购推荐，",jiage,"块一个的苹果。")
# shuiguo = 10
# print("给我来一筐，",shuiguo,"个。")
# print("打包，称重。")
# shifu = 100
# print("付款")

# def jiafa_x (a,b):
#     t=a+b
#     print("计算结果:",a,"+",b,"=",t )
#     return t
# def jianfa(a,b):
#     t=a-b
#     print("计算结果:",a,"-",b,"=",t )
#     return t
# def chengfa(a,b):
#     t = a * b
#     print("计算结果:", a, "x", b, "=", t)
#     return t
# def chufa(a,b):
#     if( b != 0):
#         t = a /b
#     else:
#         print("我就是不算！！")
#     print("计算结果:", a, "/", b, "=", t)
#     return t
# with open("D:\\software\\pycharm\\luomingxing_2019-07-17\\new_day\\paixing.txt","r") as t:
#     c=t.readlines()
#     print(c)
#     for s in c:
#          s = s.replace("\n","")
#          chufa(s)

# jiafa_x(jianfa(3,6),8)
# jianfa(3,5)
# chengfa(3,0)
# chufa(6,0)
# def urs_oudadidi(xx,uu):
#     return "{}是{}".format(xx,uu)
# print(urs_oudadidi("谁","的谁"))
#
# def ure_dd(tian,yun,sun):
#     return "{t}是{y}的{s}".format(t=tian,s=sun,y=yun,)
# print(ure_dd("她","他","优乐美"))

# 去咖啡店
# 告诉服务员要几杯咖啡
# 服务员告诉你要多少钱
# 你给服务员多少钱
# 服务员找零，给你咖啡
def cf_mi(my,cuo=1):
    print("去咖啡店")
    cuo_u = cuo
    print("告诉服务员要",cuo_u,"杯咖啡")
    print("服务员告诉你要",cuo*30,"钱")
    my_y= my
    print("你给服务员",my_y,"钱")
    print("服务员找零",my-cuo*30,"，给你",cuo,"咖啡")

cf_mi(1000,20)