# 列表进阶操作
# l*=n 将序列放n次并存入原序列
a=[1,2,3]
b=[4,5,6]
print(a+b)

a*=3
print(a)
c=a*3

# l.append(x)  将元素x他添加到序列末尾
a.append(4)
b.append(c)
print(a,b)

#l.extend(t) 列表l后面追加t输出的所有项
# 注 extend() 的添加项必须是一个可迭代对象，不能是多个元素
# eg：1,2,3就不行，但是'123'or (1,2,3)or[1,2,3]
# l.clear() 将列表的所有元素清空,

a.clear()
print()
# a.extend(1,2,3,4) 
#因为添加的不止一个元素，所以会报错
#TypeError: extend() takes exactly one argument (4 given)
print(a)

a.clear()
print()
a.extend([1,2,3,4])
print(a)

a.clear()
print()
a.extend((1,2,3,4,5))#因为a，自身就是个list，所以就算是添加的元素是tuple也会被变更为list
print(a)

# l.insert(i,x) 在列表索引的i处加入新元素x
a.insert(0,0)
print(a)

# 更新内容
# l[start:end]=t 将start:end更换为t，t为可迭代对象
a=[x for x in range(10)]
a[2:5]=[3,4,5,6] #start:end是content不是index
print(a)

# l[start:end:sep]=t 将start:end以步长为sep更换为t，t为可迭代对象

b=[x for x in range(10)]
b[::2]=['a','b','c','d','e']#此时代替换元素和替换元素的数量必须相同
print(b)

c=[x for x in range(10)]
#c[::2]=['a','b','c','d','e','f']
#此时代替换元素是5个，但是替换元素是6个会报错
#ValueError: attempt to assign sequence of size 6 to extended slice of size 5
print(b)

#l.sort(key=None,reverse=False) 对列表l进行排序，可以通过key来指定确定顺序的键值
# key是针对列表元素是非单一元素的情况下确定比较对象的
# 上面这个排序是不返回任何值的，只是对自身进行更改
# l.append(x) l.extend(x) 同上也是不返回任何值，只是对l本身作出更改
c=[2,5,6,3,1,4]
d=c.sort()
print(type(d))#运发现d <class 'NoneType'>
print(c)

# l.reverse() 对l列表排倒序
c.reverse()
print(c)
c.sort()
print(c)
c.sort(reverse=True)#sort的reverse参数为True的情况下和reverse功能一样
print(c)

#查找内容
#x in L 判断x是否在l中，返回True/False
name=['萧峰','虚竹','段誉']
if '慕容复'  not in name:
    print('你不是挂逼')

# min(l) max(l) 找出l中的min/max返回
max_c=max(c)
min_c=min(c)
print(max_c,min_c)

# L.index(x[,start[,end]]) 返回x在L中第一次出现在[start,end]的时候的index
#[,参数]这里的意思是该参数是可选参数，具体的这个里的意思就是可以指定起始值和结束值
print(name.index('虚竹'))
print(name.index('虚竹',0,2))
# 上面的意思就是在index为start=0，end=2中查询'虚竹'的index 对于待查找元素有多个想查找非第一次出现的位置时好用

# L.count(x) 返回x在L中出现的次数
print(name.count('虚竹'))

#其他操作
# L.copy() L[:] 返回一个和L一样的新列表，注是新列表 已和L无关
name_1=name.copy()
name_2=name[:]
print(name_1,name_2)

# L*n 列表L重复n次，和上面那个L*=n没啥本质区别
# 就是一个是把自己改了，一个自己没动而是作为一个计算数据
name_3=name_1*3
name_2*=3
print(name_3,name_2,name_1)

# L.pop([i]) 取出index为i的值,并将该元素返回出来，无[i]时默认取出最后一个
print(name_3.pop())
print(name_3)

# L.remove(x) 删除第一个值为x的元素,且无返回值，只改变自身
name_3.remove('萧峰')
print(name_3)

# l.clear() 将列表的所有元素清空,但无 返回值

print(type(name_3.clear()))
#del L[start:end]  L[start:end]=[]
# 把列表的start:end处清空,start:end为index且无返回值
del name_2[1: 3]
print(name_2)
name_2[0:1]=[]
print(name_2)
# del L[start:end:sep] 删除以sep为步长index 为start:end 值

del name_2[::3]
print(name_2)

# del l 删除l,不是清空l,是直接把这个元素删除
del name_2
#print(name_2) #会直接报错
#NameError: name 'name_2' is not define




























