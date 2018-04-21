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

