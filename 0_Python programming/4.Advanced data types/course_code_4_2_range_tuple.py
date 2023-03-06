# 元组是一个不可变序列
a=1, #只有一个逗号就能创建一个tuple
print(type(a))

# b=tuple(t) t是一个可以迭代的对象，但是也只能是一个元素，可以是列表，字符串，字典。但不能是多个元素

# list里改变元组的操作都不用能实现
# 但是切片是可以的，copy不支持，但是del t支持
#单独使用元组时()可以省略，只要有,就行
tianlong='萧峰',
print(type(tianlong))

#元组的拼接操作
tianlongbabu=tianlong+('虚竹','段誉')
print(tianlongbabu)

#支持全切片复制元组，但是不支持.copy()
same_tianlong=tianlongbabu[:]

print(same_tianlong)

#支持查找，但是不支持排序.sort()
print(same_tianlong.index('虚竹'))

#支持哈希 啥意思暂时不懂
print(hash(same_tianlong))

#支持整体删除，但是不支持部分删除
del tianlong
del tianlongbabu


#元组的使用场景
#在函数的返回值处使用，为了避免在大量代码中某个代码对函数返回值发生变动从而产生bug

# 实例
def get_information():
    name='虚竹'
    feature='盗号的'
    # return [name,feature]
    return name,feature

a=get_information()
# a[1]='挂逼' #如果函数返回值是list可能就会出bug
print(a)

#range 不可变序列，支持不改变自己的操作
# list tuple和range都支持取值和切片，但是list还支持查找 增加，更新，但是tuple和range都不支持 且del tuple和range也都只支持删除自身，不支持部分删除

#集合无序的保存不重复的元素，无序且不重复
#集合常用来去重
#可以通过set()来创建一个集合

a=['萧峰', '虚竹', '段誉','萧峰']
#c=set('萧峰', '虚竹', '段誉','萧峰')# 因为给set的赋值里有重复元素所以会报错
b=list(set(a))
print(b)#实现了对a的去重

# 集合支持的操作
# x in s
# x not in S
# len(S)
#上述三个操作str list tuple 也都支持

#字典
#字典的创建
a=dict(one=1,two=2,three=3)
b={'one':1,'two':2,'three':3}
c=dict(zip(['one','two','three'],[1,2,3]))#zip(s,s),将两个可迭代对象缝合为字典
d=dict([('one',1),('two',2),('three',3)])
e=dict({'one':1,'two':2,'three':3})
print(a)
print(b)
print(c)
print(d)
print(e)
#上述都是创建字典的方法，但是最常用的还是第二个

#字典的操作
# len(d)
# d[key] 返回key所对应的content
information=dict(name='虚竹',   feature='盗号的')
print(information)
print(information['name'])
# d.get(key[,default]) key对应的content返回，如果不存在改可以则返回none，如果不存在改可以则返回none，如果default有赋值则返回default
# d.pop(key[,default]) 将key对应的content从字典中删除并返回，如果不存在改可以则返回none，如果default有赋值则返回default
# d.popitem() 取出字典最后的一对key:value

print(information.get('gender','man'))
print(information.pop('name'))
print(information)
print(information.popitem())
print(information)

#d[key]=value 在字典中修改or添加一个key:value
# del d[key] 删除key以及对应的value
#key in d d中是否存在该key
#key not in d
# d.clear() 清空d，只剩一个空字典
# d.copy() 复制d,并返回

# d.keys() 返回一个可迭代对象，包括所有的key
# d.items() 返回一个可迭代对象，包括所有的key:value
# d.values() 返回一个可迭代对象，包括所有的value


# 同时循环多个列表，使用zip(lsit_1,list_2,list_n)
# for x_1,x_2,x_n in zip(lsit_1,list_2,list_n)即可
 
import random

scores=[random.randint(60,100) for x in range(10)]
student=[1+x for x in range(10)]
transcript = dict(zip(student,scores))

#传统写法
ranking= sorted(transcript.items(),key=lambda x:x[1],reverse=True)
ranked_transcript=dict(ranking)
#字典不能直接排序，必须把每个items取出之后才能排序

#python3.6+
ranked_transcript={
    k:v
    for k,v in sorted(transcript.items(),key=lambda item:item[1],reverse=True)
}
print(ranked_transcript)

students = []
for x in range(10):
    #利用ASCII码自动起名
    name='小'+chr(ord('A')+x)
    student={
    'name':name,
    'id':1+x,
    'score':random.randint(60,100)
    }
    students.append(student)#将生成的student放入students中

print(students)

students.sort(key=lambda x:x['score'],reverse=True)
for studend in students:
     print(studend['id'],studend['name'],studend['score'])





















