# 猜拳游戏
# 需求：
# 1、从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
# 2、电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
# 3、⽐较胜负



# import random
# player = input('请输入: 剪刀0、石头1、布2')
# player = int(player)
# # 产生随机整数：0、1、2 中的某一个
# computer = random.randint(0,2)
# # 用来进行测试
# # print('player=%d,computer=%d',(player,computer))
# if((player == 0) and (computer == 2)) or ((player == 1) and (computer == 2 )) or ((player == 2) and (computer == 1)):
#     print('获胜，哈哈，你太厉害了')
# elif player == computer:
#     print('平局，要不再来一局')
# else:
#     print('输了，不要走，洗洗手接着来，决战到天亮')
#
#


# 计算1~100的累加和（包含1和100）
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1

print("1~100的累积和为:%d" % sum)

# 三、计算1~100之间偶数的累加和（包含1和100）
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum +i
    i += 1

print("1~100的累积和为:%d" % sum)

# 四、打印如下图形：
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print("*", end=' ')
        j += 1
    print()
    i += 1



# 七、函数封装（一）
# 1.写一个函数打印一条横线
#
# 2.打印自定义行数的横线

def printLine():
    print("-"*30)

printLine()

# 打印多条横线
def printNumLine(num):
    i=0
    # 因为printOneLine函数已经完成了打印横线的功能，
    # 只需要多次调用此函数即可
    while i<num:
        printLine()
        i+=1


printNumLine(5)

# 八、函数封装（二）
# 1.写一个函数求三个数的和
#
# 2.写一个函数求三个数的平均值


def sum3Number(a,b,c):
    return a+b+c

# 完成对3个数求平均值
def average3Number(a,b,c):
    # 因为sum3Number函数已经完成了3个数的就和，所以只需调用即可
    # 即把接收到的3个数，当做实参传递即可
    sumResult = sum3Number(a,b,c)
    aveResult = sumResult/3.0
    return aveResult

result = sum3Number(1,2,3)
print(result)

print(average3Number(12,2,32))


# 学生的信息可以使用一个字典类型
# 管理学生可以使用列表

# 定义全局变量学生列表
student_list = [] # list()
# print("全局变量:", id(student_list))

# 显示功能菜单的函数
def show_menu():
    print("-----学生管理系统v1.0-----")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出")


# 添加学生
def add_student():
    name = input("请输入学生的姓名:")
    age = input("请输入学生的年龄:")
    sex = input("请输入学生的性别:")

    # 定义学生字典类型的变量
    student_dict = {} # dict()
    # 把学生的信息使用字典进行存储
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["sex"] = sex
    # 这里可以不使用global因为列表是可变类型，可以在原有数据的基础上进行修改，内存地址不变
    # 因为列表的内存地址不变，全局变量不需要使用global
    # 加上global表示内存地址要发生变化

    # 把学生信息添加到学生列表中
    student_list.append(student_dict)
    # global student_list
    # # student_list = [{'name': "李四", "age":"18", "sex":"男"}]
    # student_list.append(student_dict)


# 显示所有学生信息
def show_all_student():
    # print(student_list, id(student_list))
    for index, student_dict in enumerate(student_list):
        # 学号和下标的关系
        student_no = index + 1

        print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                           student_dict["age"], student_dict["sex"]))


# 删除学生信息
def remove_student():
    student_no = int(input("请输入要删除学生的学号:"))
    # 获取学生字典信息的下标
    index = student_no - 1
    if index >= 0 and index < len(student_list):
        # 根据下标删除学生信息
        del student_list[index]
    else:
        print("请输入正确的学号")

# 修改学生信息
def modify_student():
    student_no = int(input("请输入要修改学生的学号:"))
    # 根据学号计算下标
    index = student_no - 1

    if index >= 0 and index < len(student_list):
        # 根据下标获取学生字典信息
        student_dict = student_list[index]

        name = input("请输入您修改后的名字:")
        age = input("请输入您修改后的年龄:")
        sex = input("请输入您修改后的性别:")

        student_dict["name"] = name
        student_dict["age"] = age
        student_dict["sex"] = sex
    else:
        print("请输入正确的学号")


# 查询学生
def search_student():
    name = input("请输入要查询的学生姓名:")

    # 遍历学生列表信息
    for index, student_dict in enumerate(student_list):
        # pass # 空实现
        if student_dict["name"] == name:
            student_no = index + 1
            # 说明找到了这个学生
            print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                               student_dict["age"], student_dict["sex"]))
            break
    else:
        print("对不起，没有找到这个学生")

# 程序启动的函数
def run():

    while True:
        # 显示功能菜单
        show_menu()
        # 接收用户的指令
        menu_option = input("请输入您需要的功能选项:")

        if menu_option == "1":
            print("添加学生")
            add_student()
        elif menu_option == "2":
            print("删除学生")
            remove_student()
        elif menu_option == "3":
            print("修改学生信息")
            modify_student()
        elif menu_option == "4":
            print("查询学生信息")
            search_student()
        elif menu_option == "5":
            print("显示所有学生信息")
            show_all_student()
        elif menu_option == "6":
            print("退出")
            break

# 执行程序启动的函数
run()

















