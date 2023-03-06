import pandas as pd
# Series用法演示
s= pd.Series([1,2,3,4,5])

print(s)

s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# 可以加入index来添加序列
s2 = pd.Series({'a'':' 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# 也可以使用字典的方式
print(s1,s2)
