# u使用列表推导式生成1-10
name=[1+i for i in range(0,10)]
print(name)
# 新增一个数35
name.append(35)
print(name)
# 新增一批数20-30
name.extend(range(20,31))
print(name)
# 把0塞到最前面
name.insert(0,0)
print(name)
# 把第五个到第十个数给改成45-50
name[5:10]=[x for x in range(45,51)]
print(name)
# 有步长的更改三个数值
name[1:7:2]=[y for y in range(70,73)]
print(name)
# 排序和倒叙
name.sort()
print(name)
name.reverse()
print(name)
name.sort()
print(name)
name.sort(reverse=True)
print(name)
# 判断某个数字是否在列表中
if 2 in name:
    print('在')

# 移除上面能数字
name.remove(2)
print(name)
# 清空列表
del name[:]
print(name)
# 删除列表
del name
# print(name)
