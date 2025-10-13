a=0
while a<10:
    a += 1
    print(a)
# 1. 使用while循环打印1到10的数字
print("---------")
a=0
while a<10:
    a += 1
    if(a%2==0):
        if(a==8):
            print("8往后就断了")
            break
        print(a)
print("偶数循环")    
print("---------")

# while循环结束衔接else，作用是在循环结束后执行else里的操作。(break结束的循环不会执行else)
a=0
while a<10:
    a += 1
    if(a%2!=0):
        if(a==5):
            print("跳过5")
            continue
        print(a)
  
else:
    print("循环结束")
print("奇数循环")  
# while True:
#     print("死循环")
# a = 5
# print("《《猜数字游戏》》")
# while True:
#     b = int(input("请输入一个数："))
#     if b>a:
#         print("大了")
#     elif b<a:
#         print("小了")
#     else:
#         print("猜对了")
#         break

for i in range(1,11):
    print(i)
else:
    print("打印1到10的数")