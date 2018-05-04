########################################################
#####                 第五章                     #######
########################################################

from pandas import Series, DataFrame

import pandas as pd

import numpy as np
#####$$Series$$#####

obj = Series([4,7,-5,3])

obj2 = Series([4,7,-5,3], index=['d', 'b', 'a', 'c'])

'b' in obj2

sdata = {'Ohio' : 35000, 'Texas' : 71000, 'Oregon' : 16000, 'Utah' : 5000}
obj3 = Series(sdata)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = Series(sdata, index=states)

pd.isnull(obj4)
pd.notnull(obj4)

obj4.isnull()

obj4.name = 'population'


obj4.index.name = 'state'

obj.index = ['California', 'Ohio', 'Oregon', 'Texas']

data = {
'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year' :[2000, 2001, 2002, 2001, 2002],
'pop' : [1.5,1.7,3.6,2.4,2.9]
}

frame = DataFrame(data)

DataFrame(data, columns=['year', 'state', 'pop'])

frame2 = DataFrame(data, columns = ['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])

frame2.columns

frame2['state']

frame2.year

frame2.ix['three']

frame2.loc['three']

frame2['debt'] = 16.5

frame2['debt'] = np.arange(5)

val = Series([-1.2,-1.5,-1.7], index=['two', 'four', 'five'])

frame2['eastern'] = frame2.state == 'Ohio'

del frame2['eastern']

pop = {
'Nevada' : {2001 : 2.4, 2002:2.9},
'Ohio': {2000:1.5, 2001:1.7, 2002:3.6}
}

frame3 = DataFrame(pop)

DataFrame(pop, index=[2001, 2002, 2003])

pdata = {'Ohio': frame3['Ohio'][:-1],
'Nevada': frame3['Nevada'][:2]
}

frame3.index.name = 'year'; frame3.columns.name = 'state'

frame3.values #跟Series一样，values属性也会以二维ndarray的形式返回DataFrame中的数据

obj = Series(range(3), index=['a', 'b', 'c'])

index = obj.index #index不可修改

index[1:]

index = pd.Index(np.arange(3))

obj2 = Series([1.5,-2.5,0], index = index)

obj2.index is index

obj = Series([4.5,7.2,-5.3,3.6], index=['d', 'b', 'a', 'c'])

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

obj3 = Series(['blue', 'purple', 'yellow'], index = [0,2,4])

obj3.reindex(range(6), method= 'ffill') #向前填充

frame = DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'], columns = ['Ohio', 'Texas' , 'California'])

frame2 = frame.reindex(['a', 'b', 'c', 'd'])

states = ['Texas', 'Utah', 'California']

frame.reindex(columns = states)

#frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=states)

frame.reindex(index=['a', 'b', 'c', 'd'], method= 'ffill') #正确写法

obj = Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])
 
new_obj = obj.drop('c')

data = DataFrame(np.arange(16).reshape((4,4)), index = ['Ohio','Colorado','Utah','New York'], columns = ['one', 'two', 'three', 'four'])

data.drop(['Colorado','Ohio'])

data.drop('two', axis = 1) #不改变data的值

data.drop(['two', 'four'], axis=1)

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

obj['b']

data[:2]

data[data['three']>5]

data[data<5.] = 0

data. ix[['Colorado','Utah'], [3,0,1]]

data.iloc[2]

data.loc[:'Utah', 'two']

data.ix[data.three > 5, :3]

s1 = Series([7.3,-2.5,3.4,1.5], index=['a', 'c', 'd', 'e'])

s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

df1 = DataFrame(np.arange(9.).reshape((3,3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])

df2 = DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

#####$$在算数方法中填充值$$#####
df1 = DataFrame(np.arange(12.).reshape((3,4)), columns=list('abcd'))

df2 = DataFrame(np.arange(20.).reshape((4,5)), columns=list('abcde'))

df1 + df2

df1.reindex(columns=df2.columns, fill_value=0)

#####$$DataFrame和Series之间的运算$$#####
arr = np.arange(12.).reshape((3,4))
arr - arr[0]

frame = DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.iloc[0]

frame

data = DataFrame(np.arange(16).reshape((4,4)), index = ['Ohio','Colorado','Utah','New York'], columns = ['one', 'two', 'three', 'four'])

frame - series
series2 = Series(range(3), index=['b', 'e', 'f'])
frame + series2

series3 = frame['d']



# fig = plt.figure()

# for i in range(0,4):
	# fig.add_subplot(2,2,i + 1)
	# plt.plot(data.iloc[:,i])
	# plt.title(data.index[i])
# plt.show()
	
# output = open('data.txt', 'w+')
# str = ""


#####$$函数和映射$$#####
frame = DataFrame(np.random.randn(4,3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon']

# result:
               # b         d         e
# Utah   -0.602319  1.261217  0.927547
# Ohio   -0.162878 -0.413711 -0.341497
# Texas  -0.736304 -0.956781  0.167785
# Oregon  1.740673  0.427462  0.359928
frame

np.abs(frame)
# result:
               # b         d         e
# Utah    0.602319  1.261217  0.927547
# Ohio    0.162878  0.413711  0.341497
# Texas   0.736304  0.956781  0.167785
# Oregon  1.740673  0.427462  0.359928



In [18]: f=lambda x: x.max() - x.min()

In [19]: frame.apply(f)
Out[19]:
b    2.476977
d    2.217998
e    1.269044
dtype: float64

In [20]: frame.apply(f, axis = 1)
Out[20]:
Utah      1.863536
Ohio      0.250832
Texas     1.124566
Oregon    1.380745
dtype: float64


In [22]: def f(x):
    ...:     return Series([x.min(), x.max()], index=['min', 'max'])
    ...:

In [23]: frame.apply(f,axis=1)
Out[23]:
             min       max
Utah   -0.602319  1.261217
Ohio   -0.413711 -0.162878
Texas  -0.956781  0.167785
Oregon  0.359928  1.740673

In [24]: frame.apply(f)
Out[24]:
            b         d         e
min -0.736304 -0.956781 -0.341497
max  1.740673  1.261217  0.927547

# applymap用于DataFrame， map用于Series

In [26]: format = lambda x: '%.2f'%x

In [27]: frame.applymap(format)
Out[27]:
            b      d      e
Utah    -0.60   1.26   0.93
Ohio    -0.16  -0.41  -0.34
Texas   -0.74  -0.96   0.17
Oregon   1.74   0.43   0.36

In [28]: frame['e'].map(format)
Out[28]:
Utah       0.93
Ohio      -0.34
Texas      0.17
Oregon     0.36
Name: e, dtype: object


#####$$排序和排名$$#####


In [30]: obj = Series(range(4), index=['d', 'a', 'b', 'c'])

In [31]: obj.sort_index()
Out[31]:
a    1
b    2
c    3
d    0
dtype: int64

frame = DataFrame(np.arange(8).reshape((2,4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])

obj = Series([4,7,-3,2])
obj.sort_values()
obj = Series([4, np.nan, 7, np.nan, -3, 2])

frame = DataFrame({'b':[4,7,-3,2], 'a':[0,1,0,1]})

frame.sort_index(by=['a', 'b'])

obj.rank(method='first', na_option='bottom') #排序

#####$$带重复值的轴索引$$#####

obj = Series(range(5), index=['a', 'a' , 'b', 'b', 'c'])

In [8]: obj.index.is_unique
Out[8]: False

In [12]: df = DataFrame(np.random.randn(4,3), index = ['a', 'a' , 'b', 'b'])

In [13]: df
Out[13]:
          0         1         2
a -1.049870  0.405578  0.256445
a -1.391671 -1.057513  0.699057
b -0.318720  0.128407  0.292529
b  0.002353  2.884667  1.344446

In [14]: df.loc['b']
Out[14]:
          0         1         2
b -0.318720  0.128407  0.292529
b  0.002353  2.884667  1.344446

df = DataFrame([[1.4,np.nan], [7.1,-4.5],[np.nan,np.nan], [0.75,-1.3]], index = ['a', 'b', 'c', 'd'], columns=['one', 'two'])

df.sum()

#描述统计值

In [25]: df.describe()
Out[25]:
            one       two
count  3.000000  2.000000
mean   3.083333 -2.900000
std    3.493685  2.262742
min    0.750000 -4.500000
25%    1.075000 -3.700000
50%    1.400000 -2.900000
75%    4.250000 -2.100000
max    7.100000 -1.300000

#####$$相关系数和协方差$$#####

#由于yahoo财经数据迁移数据提取不到，暂时未做

#####$$唯一值，值计数以及成员资格$$#####
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

obj.value_counts()

pd.value_counts(obj.values, sort=False)

data = DataFrame(
{'Qu1': [1,3,4,3,4],
"Qu2" : [2,3,1,2,3],
"Qu3" : [1,5,2,4,4]
}
)


In [23]: data = DataFrame(^M
    ...: {'Qu1': [1,3,4,3,4],^M
    ...: "Qu2" : [2,3,1,2,3],^M
    ...: "Qu3" : [1,5,2,4,4]^M
    ...: }^M
    ...: )

In [24]: data
Out[24]:
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    4    3    4

In [25]: data.apply(pd.value_counts)
Out[25]:
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  NaN  2.0  1.0
3  2.0  2.0  NaN
4  2.0  NaN  2.0
5  NaN  NaN  1.0

In [26]: data.apply(pd.value_counts).fillna(0)
Out[26]:
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0

#####$$处理缺失值$$#####

string_data = Series(['abc', 'bcd', np.nan, 'def'])


In [40]: string_data.isnull
Out[40]:
<bound method Series.isnull of 0    None
1     bcd
2     NaN
3     def
dtype: object>

In [41]: string_data.isnull()
Out[41]:
0     True
1    False
2     True
3    False
dtype: bool


#####$$滤除缺失数据$$#####

from numpy import nan as NA

data = Series([1, NA, 3.5, NA, 7])

In [10]: data.dropna()
Out[10]:
0    1.0
2    3.5
4    7.0
dtype: float64

In [11]: data[data.notnull()]
Out[11]:
0    1.0
2    3.5
4    7.0
dtype: float64

data = DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])

In [15]: data.dropna(how = 'all')
Out[15]:
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
3  NaN  6.5  3.0

In [16]: data[4] = NA

In [17]: data
Out[17]:
     0    1    2   4
0  1.0  6.5  3.0 NaN
1  1.0  NaN  NaN NaN
2  NaN  NaN  NaN NaN
3  NaN  6.5  3.0 NaN

In [18]: data.dropna(axis = 1, how ='all')
Out[18]:
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0

df = DataFrame(np.random.randn(7,3))

df.iloc[:4,1] = NA; df.ix[:2, 2] = NA

In [23]: df.dropna(thresh = 2)
Out[23]:
          0         1         2
3 -0.358241       NaN -0.670095
4  0.023879  1.523128 -3.034558
5  0.949051 -0.624230  0.366703
6 -0.748698  0.133064 -0.654409

In [24]: df.dropna(thresh = 3)
Out[24]:
          0         1         2
4  0.023879  1.523128 -3.034558
5  0.949051 -0.624230  0.366703
6 -0.748698  0.133064 -0.654409


#####$$填充缺失数据$$#####
In [25]: df.fillna(0)
Out[25]:
          0         1         2
0 -0.407754  0.000000  0.000000
1 -0.119154  0.000000  0.000000
2  1.113036  0.000000  0.000000
3 -0.358241  0.000000 -0.670095
4  0.023879  1.523128 -3.034558
5  0.949051 -0.624230  0.366703
6 -0.748698  0.133064 -0.654409

In [26]: df.fillna({1:0.5,3:-1})
Out[26]:
          0         1         2
0 -0.407754  0.500000       NaN
1 -0.119154  0.500000       NaN
2  1.113036  0.500000       NaN
3 -0.358241  0.500000 -0.670095
4  0.023879  1.523128 -3.034558
5  0.949051 -0.624230  0.366703
6 -0.748698  0.133064 -0.654409

#总是返回被填充对象的引用，inplace起到的作用
In [27]: _ = df.fillna(0, inplace=True)

In [28]: df
Out[28]:
          0         1         2
0 -0.407754  0.000000  0.000000
1 -0.119154  0.000000  0.000000
2  1.113036  0.000000  0.000000
3 -0.358241  0.000000 -0.670095
4  0.023879  1.523128 -3.034558
5  0.949051 -0.624230  0.366703
6 -0.748698  0.133064 -0.654409

In [29]: df = DataFrame(np.random.randn(6,3))

In [30]: df.iloc[:2,1] = NA

In [31]: df.iloc[4:, 2] = NA

In [34]: df.fillna(method = 'ffill')
Out[34]:
          0         1         2
0 -0.403845       NaN -1.517180
1 -0.498031       NaN  0.390021
2 -1.257538 -1.470415 -0.585982
3 -1.172443  0.065520  0.535849
4  2.572929  0.102688  0.535849
5  0.493872  0.833607  0.535849

In [37]: df.fillna(method='bfill')
Out[37]:
          0         1         2
0 -0.403845 -1.470415 -1.517180
1 -0.498031 -1.470415  0.390021
2 -1.257538 -1.470415 -0.585982
3 -1.172443  0.065520  0.535849
4  2.572929  0.102688       NaN
5  0.493872  0.833607       NaN


#####$$层次化索引$$#####

 data = Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1,2,3,1,2,3,1,2, 2,3]])
 
 In [40]: data
Out[40]:
a  1    0.274084
   2   -1.190673
   3   -0.418101
b  1   -0.719831
   2    1.559763
   3    1.128530
c  1   -0.302453
   2    0.255061
d  2    1.462377
   3   -0.651053
dtype: float64

frame = DataFrame(np.arange(12).reshape((4,3)), index=[['a','a','b','b'],[1,2,1,2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])


In [60]: frame.index.names = ['key1', 'key2']

In [61]: frame.columns.names = ['state', 'color']

In [62]: frame
Out[62]:
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
	 

pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=['state', 'color'])


#####$$重排分级顺序$$#####
frame.swaplevel('key1', 'key2')


In [70]: frame.swaplevel('key1', 'key2')
Out[70]:
state      Ohio     Colorado
color     Green Red    Green
key2 key1
1    a        0   1        2
2    a        3   4        5
1    b        6   7        8
2    b        9  10       11

In [71]: frame.sortlevel(1)
D:\Python27\Scripts\ipython:1: FutureWarning: sortlevel is deprecated, use sort_index(level= ...)
Out[71]:
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
b    1        6   7        8
a    2        3   4        5
b    2        9  10       11

In [72]: frame.swaplevel(0,1).sortlevel(0)
D:\Python27\Scripts\ipython:1: FutureWarning: sortlevel is deprecated, use sort_index(level= ...)
Out[72]:
state      Ohio     Colorado
color     Green Red    Green
key2 key1
1    a        0   1        2
     b        6   7        8
2    a        3   4        5
     b        9  10       11

#####$$根据汇总级别统计$$#####


In [77]: frame.sum(level='key2')
Out[77]:
state  Ohio     Colorado
color Green Red    Green
key2
1         6   8       10
2        12  14       16

In [78]: frame.sum(level='color', axis=1)
Out[78]:
color      Green  Red
key1 key2
a    1         2    1
     2         8    4
b    1        14    7
     2        20   10
	 
#####$$使用DataFrame的列$$#####

frame = DataFrame({'a':range(7), 'b':range(7,0,-1), 'c' : ['one','one','one','two','two','two','two'], 'd':[0,1,2,0,1,2,3]})

#设置索引
In [83]: frame.set_index(['c', 'd'])
Out[83]:
       a  b
c   d
one 0  0  7
    1  1  6
    2  2  5
two 0  3  4
    1  4  3
    2  5  2
    3  6  1

#取消索引
In [85]: frame.reset_index()
Out[85]:
   index  a  b    c  d
0      0  0  7  one  0
1      1  1  6  one  1
2      2  2  5  one  2
3      3  3  4  two  0
4      4  4  3  two  1
5      5  5  2  two  2
6      6  6  1  two  3

#####$$整数索引$$#####
#对于标签值有效
In [89]: ser2 = Series(np.arange(3.), index=['a','b','c'])

In [90]: ser2[-1]
Out[90]: 2.0


In [94]: ser3.iloc[2]
Out[94]: 2

In [95]: ser3.loc[-5]
Out[95]: 0