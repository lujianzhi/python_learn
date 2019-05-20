import function_py as t1  # 导包并且别名
import sys
sys.path[0] = '/home/ian/development/python/project/python_learn/sub' # 为了找到另外文件夹下的模块,修改路径
import sub_function_py as t2  # 导其他文件夹下的包并且别名

# 第一个python项目
p = 0
p = '11s'
print(p)

d1 = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
print(d1)
d2 = d1.popitem()
print(d2)
for d_T in d1.items():
    print(d_T)

a = 'hello world'
print(a[4:7])
print(a[-7:-4])
del (a)

b = 'C:\back\name'
print(b)
print(R'C:\back\name')

c = 'Tom'
d = 10
print("%s is %d years old" % (c, d))

if False:
    print("1")
    print("2")
    print("3")
print("4")

e = 10
if e <= 4:
    print("e<=4")
elif e < 9:
    print("e<4")
else:
    print("e>=9")

numbers = '1,2,3,4,5,6,7,8,9'
for i in numbers:
    if i == '4':
        print(i)

for i in range(10):
    print("第一次:%d" % (i))
    i += i
    print(i)

if "3" not in numbers:
    print("not in")
else:
    print("in")

print(id(numbers))
print(id(e))


def find_2():
    array = [1, 2, 3, 4, 5]
    for i in array:
        if (i == 2):
            print('有2')
            break


find_2()

array = [1, 2, 3, 4, 5]

print(t1.find_number(array, "5"))  # 使用导进来的包调用函数
print(t2.find_number(array, "5"))  # 使用导进来的包调用函数