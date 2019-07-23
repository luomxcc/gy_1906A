# # 第四周！第一天课程！！
# b = "https://www.baidu.com/"
# print(b.split('://'))
# print(b.split('://')[0])
# uir =b.split('://')[1]
# print(uir)
# 域名地址截取
# dizi = "http://qa.yansl.com:8080/swagger-ui.html"
#
# print(dizi.split("://"))
# xieyi = dizi.split("://")[0]
# print(xieyi)
# ip = dizi.split("://")[1]
# print(ip.find(':'))
# print([ip.find(':')])
# print(ip)
# print(ip.find('/'))
# print(ip[:17])
# print((ip[ip.find('/'):]))
# 列表 创建一个例表
# lie=[]
# 往列表内插入一个数据
# lie.append(1)
# lie.append(2)
# lie.append(8)
# lie.append('leiji')

# 创建
# lei =[]
# lei.append(2)
# lei.append('wqe')
# # lei.append('wwww')
# 合并两个列表
# print(lie+lei)
# 生成一个新列表
# lei.extend(lie)
# 把后面一个列表数据 插入前面列表中
# print(lei)
# 根据下标删除列表中的数据，不给下标位默认删除最后一个数据。
#lei.clear()清空整个列表
# lei.pop(1)
# print(lei)
# 改列表数据,根据数据下标，修改某个值
# lei[下标]=修改的值
# 查 根据下标查询
# print(lei[下标])
# 截取部分数据
# print(lei[:2:])
# 求例表字符串长度
# print(len(lei))
# 成员判断,
# if("www" in lei):
#     print("找我干啥？")
# else:
    # print("起开，没有这个人、")
# 元组 元组中只有一个数据，最后需要有逗号
# b = (1,)
# a = (2,3,4,5,6)
# 元组总数据不能做修改

# 元组合并
# print(a+b)
# 截取
# print(a[:1])
# 成员判断
# if("www" in a):
#     print("找我干啥？")
# else:
#     print("起开，没有这个人、")
# 查看 根据下标进行查看
# print(a[2])
# for i in a:
#     print(i)
# print(len(a))

# 字典 创建
# a = { }
# 新增数据
# a["性别"] = "没有"
# print(a)
# 对字典进行修改，字典中key是惟一的，不允许出现两次，2、key不可以被改变，
# a["手机号码"] ="13545872121"
# print(a)
# 删除字典某一对值、
# a.pop('年龄')
# print(a)
# 清空一个字典
# a.clear()
# print(a)
# 两个字典合并
# b = {"外号":"死鬼","姓名":"杨白劳"}
# a.update(b)
# print(a)
# 合并两个字典，并生成一个的字典
# print(dict(a,**b))
# print(a)
# print(b)

'''
按照扑克牌的规则，现在有6张牌，只要5张
黑桃（S）红桃（H）方块（D）梅花（C）
牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

'''
# a = '''["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]'''
# a = a.replace('"',"''")
# print(a[3:-3])
# print(a)
# a = a[3:-3]
# b = a.split("'' , ''")
# print(b)
# c = { }
# print(c)
# for i in b :
#     f=(i[1:])
#     print(f)
#     if(f in c):
#         c[f]+= 1
#     else:
#         c[f] = 1
# print(c)
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# 第一步：统一符号  对字符串的处理，用replace（）
def pukepai_3_2():
    a = input("赶紧出牌：")
    a =a.replace('"',"''")
    # print(a)
    # 第二步：去掉中括号 字符串截取  [::]
    a = a[3:-3]
    # print(a)
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    b = a.split("'' , ''")
    # print(b)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    k = {}
    for s in b :
        x = s[1:]
        # print(x)
    # 第五步：统计相同的数字个数  用字典去统计
        if(x in k ):
            k[x] +=1
        else:
            k[x] = 1
    # print(k)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    # 如果key对应的数值有3的 v1 = 1，如果没有则为0
    # 如果key对应的数值有2的 v2 = 1，如果没有则为0
    v1 = 0
    v2 = 0
    for key in k:
        if(k[key] == 3):
            v1 = 1
        if(k[key] == 2):
            v2 = 1
    if(v1 == 1 and v2 == 1):
        print("三带二，收钱")
    else:
        print("要不起，走开")

for i in range(3):
    pukepai_3_2()
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
