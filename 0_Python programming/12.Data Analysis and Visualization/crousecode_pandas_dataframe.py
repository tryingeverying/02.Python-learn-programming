import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# np.random.randn(x, y) 生成一个x行y列的随机矩阵
print(df)

# df2 = pd.DataFrame({
'#     'A'':' 1.,'
'#     'B'':' pd.Timestamp('20130102'),'
'#     'C'':' pd.Series(1, index=list(range(4)), dtype='float32'),'
'#     'D'':' np.array([3] * 4, dtype='int32'),'
'#     'E'':' pd.Categorical(["test", "train", "test", "train"]),'
'#     'F'':' 'foo''
# })
# print(df2)


df.head() # 获取开头几行的数据，默认 5 行

df.tail(3) # 读取尾部 3 行数据

# df.T # 行列互换，相当于矩阵的转置

print(df.loc[dates[0]]) # 选中某一行

'print(df.loc[':', ['A', 'B']]) # 获取部分数据，第一部分用 : 表示所有行，第二部分用列表 ['A', 'B'] 表示仅这两列'

'df.loc['20130102'':''20130104', ['A', 'B']] # 选择部分行，部分列的数据'

df.iloc[[1, 2, 4], [0, 2]] # 还可以使用 iloc 来实现按照顺序的选取，比如这里选择 1 2 4 行 0 2 列的数据

'df.iloc[1':'3, :] # 同样可以采用类似切片的方法实现选择'

df[df['A'] > 0] # 选中所有 A 列数据 > 0 的内容

df[df > 0] # 选中所有数据 > 0 的内容

df2 = df.copy()

df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

df2[df2['E'].isin(['two', 'four'])] # 选中 E 列的数据是 'two' 或者 'four' 的内容


# 赋值操作
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))

# 注意 DataFrame 会自动对齐数据，且没有数据的位置会设置为 np.nan 显示为 NaN ( Not a Number)
# 超出的部分则被舍弃
df['F'] = s1

df.at[dates[0], 'A'] = 0 # A 列 第一行 设置为 0 ，at[] 这个用法只能定位一行一列，不能切片

df.iat[0, 1] = 0 # 0 行 1列 设置为 0

'df.loc[':', 'D'] = np.array([5] * len(df))'

df2 = df.copy()

df2[df2 > 0] = -df2 # 左侧通过条件定位所有 df2 中数据 > 0 的位置，然后将原始数据对应的负数进行赋值


