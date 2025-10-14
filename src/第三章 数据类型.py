a = 12.3
print(type(a))
# type 查看数据类型s

# Name = input("请输入姓名：")
# print('你好,%s' % Name)
# # %s占位符

na = "abc"
me = 'def'
name = na + me
print(na+me)
print(na*3)
# 字符串拼接

print(name[0:])

print(len(name))

print('a' in name)
# 成员运算 in 判断是否在字符串里

#列表 =》 存储多个值 有序 可变类型 (类似于数组)

li = [1,2,3,4,5]
li.append(0)   #列尾追加数据
print(li)
li.extend([6,7,8])  #
print(li)

#列表删除 =》 remove 删某一个元素  clear 清空列表里面的值  del 通用删除，甚至可删整个列表
li.remove(1)
print(li)
# li.clear()
# print(li)
# del li
# print(li)  #报错 因为已经删了

# for i,x in enumerate(li):
#     print(i,x)

# lis1 = [1,2,3,4,5,[6,7,8, ]]
# lis2 = lis1
# lis1.append(9)
# print(lis1)
# print(lis2)
# lis1[5][2] = 10
# print(lis2)


# #浅拷贝 =》 copy() 复制一个新的列表 但是如果列表里有嵌套列表，嵌套列表内还是指向同一块内存地址
li1 = [1,2,3,4,5,[6,7,8, ]]
# li2 = li1.copy() #浅拷贝
# print(li2,"------")
# li1[5].append(6)    #增值后浅拷贝发生变化 与li1指向同一块内存
# print(li2)
# print(li1,"----")
# li1.append(9)       #增值后浅拷贝不变 与li1指向不同内存

# print(li1)
# print(li2)
# li1.pop()  #删除列尾元素 li1删除数据不会影响li2
# li1.pop()

# print(li1)
# print(li2)

#深拷贝 =》  copy.deepcopy() 完全复制一个新的列表，两者互不影响
import copy
li3 = copy.deepcopy(li1)
print(li3,"------")
li1[5].append(6)    #增值后深拷贝不变 与li1指向不同内存
print(li3)
print(li1,"----")

li1.pop()     #删除列尾元素 li1删除数据不会影响li3
print(li1)
print(li3)


#元组：（）  存多个值 值不可变 (类似于常量数组) 主要用来读取数据
age = (11,22,33,44,55)
print(age)

#字典：{}   无序 可变类型  key:value 键值对
ls = {'name':'张三','age':18}
print(ls)
#fromkeys()  创建一个新字典 
an = ls.fromkeys(ls,'i an Albert')   #用字典的key创建一个新字典，value都为后面指定的值
print(an)
print(ls["age"])   
ls['sex'] = '男'   #新增键值对
print(ls)

#集合：{}  无序 不重复元素  可变类型 值唯一 
piano = {'albert','孙悟空','周星驰','朱雷','林志玲'}    #钢琴学员
violin = {'第八城','郭德纲','林忆莲','周星驰'}          #小提琴学员
#集合运算
print(piano & violin)   #交集  报钢琴和小提琴都有的学员
print(piano | violin)   #并集  两者所有学员
print(piano - violin)  #差集   只报钢琴的学员
print(piano ^ violin)  #补集   没有重复的学员