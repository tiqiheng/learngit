#####$$数据库风格的DataFrame合并$$#####

import pandas as pd
from pandas import Series, DataFrame
df1 = DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1' : range(7)})
df2 = DataFrame({'key' : ['a','b', 'd'], 'data2' : range(3)})

In [270]: DataFrame.merge(df1, df2)
Out[270]:
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0

df3 = DataFrame({'lkey':['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1' : range(7)})

df4 = DataFrame({'rkey' : ['a','b', 'd'], 'data2' : range(3)})

In [274]: pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey', how = 'outer')
     ...:
Out[274]:
   data1 lkey  data2 rkey
0    0.0    b    1.0    b
1    1.0    b    1.0    b
2    6.0    b    1.0    b
3    2.0    a    0.0    a
4    4.0    a    0.0    a
5    5.0    a    0.0    a
6    3.0    c    NaN  NaN
7    NaN  NaN    2.0    d

df1 = DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'b'], 'data1' : range(6)})

df2 = DataFrame({'key' : ['a','b', 'a', 'b', 'd'], 'data2' : range(5)})

In [278]: pd.merge(df1, df2, how='left')
Out[278]:
    data1 key  data2
0       0   b    1.0
1       0   b    3.0
2       1   b    1.0
3       1   b    3.0
4       2   a    0.0
5       2   a    2.0
6       3   c    NaN
7       4   a    0.0
8       4   a    2.0
9       5   b    1.0
10      5   b    3.0

In [279]: pd.merge(df1, df2, how='right')
Out[279]:
    data1 key  data2
0     0.0   b      1
1     1.0   b      1
2     5.0   b      1
3     0.0   b      3
4     1.0   b      3
5     5.0   b      3
6     2.0   a      0
7     4.0   a      0
8     2.0   a      2
9     4.0   a      2
10    NaN   d      4

left = DataFrame({'key1':['foo', 'foo', 'bar'],
'key2':['one', 'two', 'one'],
'lval':[1,2,3]
})

right = DataFrame({'key1':['foo', 'foo', 'bar', 'bar'],
'key2':['one', 'one', 'one', 'two'],
'lval':[4,5,6,7]
})

pd.merge(left, right, on=['key1', 'key2'], how='outer')



In [286]: pd.merge(left, right, on = 'key1')
Out[286]:
  key1 key2_x  lval_x key2_y  lval_y
0  foo    one       1    one       4
1  foo    one       1    one       5
2  foo    two       2    one       4
3  foo    two       2    one       5
4  bar    one       3    one       6
5  bar    one       3    two       7


#####$$索引上的合并$$#####
left1 = DataFrame({'key':['a', 'b','a','a','b','c'],
'value':range(6)
})

right1 = DataFrame({'group_val':[3.5,7]}, index=['a', 'b'])

In [295]: pd.merge(left1, right1, left_on='key', right_index=True)
Out[295]:
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0

In [296]: pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
Out[296]:
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0
5   c      5        NaN

lefth = DataFrame({'key1':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'key2':[2000, 2001,2002,2001,2002],
'data':np.arange(5.)
})

righth = DataFrame(np.arange(12).reshape((6,2)), index=[['Nevada','Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], [2001,2000,2000,2000,2001,2002]],columns=['event1', 'event2']
)

In [307]: pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
Out[307]:
   data    key1  key2  event1  event2
0   0.0    Ohio  2000       4       5
0   0.0    Ohio  2000       6       7
1   1.0    Ohio  2001       8       9
2   2.0    Ohio  2002      10      11
3   3.0  Nevada  2001       0       1

left2 = DataFrame([[1.,2.],[3.,4.],[5.,6.]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])

right2 = DataFrame([[7.,8.],[9.,10.],[11.,12.],[13,14]], index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Nevada'])

#####$$轴向链接$$#####

In [321]: arr = np.arange(12.).reshape((3,4))

In [322]: arr
Out[322]:
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])

In [323]: np.concatenate([arr,arr],axis=1)
Out[323]:
array([[ 0.,  1.,  2.,  3.,  0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.,  4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.,  8.,  9., 10., 11.]])

s1 = Series([0,1], index = ['a', 'b'])
s2 = Series([2,3,4], index = ['c', 'd', 'e'])
s3 = Series([5,6], index = ['f', 'g'])

In [329]: pd.concat([s1,s2,s3], axis=1)
Out[329]:
     0    1    2
a  0.0  NaN  NaN
b  1.0  NaN  NaN
c  NaN  2.0  NaN
d  NaN  3.0  NaN
e  NaN  4.0  NaN
f  NaN  NaN  5.0
g  NaN  NaN  6.0

In [330]: pd.concat([s1*5,s3])
Out[330]:
a    0
b    5
f    5
g    6
dtype: int64

In [331]: s4=pd.concat([s1*5,s3])

In [332]: pd.concat([s1,s4])
Out[332]:
a    0
b    1
a    0
b    5
f    5
g    6
dtype: int64

In [333]: pd.concat([s1,s4],axis=1)
Out[333]:
     0  1
a  0.0  0
b  1.0  5
f  NaN  5
g  NaN  6

In [334]: pd.concat([s1,s4],axis=1,join='inner')
Out[334]:
   0  1
a  0  0
b  1  5

pd.concat([s1,s4], axis=1,join_axes=[['a', 'c', 'b', 'e']])


In [334]: pd.concat([s1,s4],axis=1,join='inner')
Out[334]:
   0  1
a  0  0
b  1  5

In [335]: pd.concat([s1,s4], axis=1,join_axes=[['a', 'c', 'b', 'e']])
Out[335]:
     0    1
a  0.0  0.0
c  NaN  NaN
b  1.0  5.0
e  NaN  NaN

result = pd.concat([s1,s1,s3],keys=['one', 'two', 'three'])

In [338]: result.unstack()
Out[338]:
         a    b    f    g
one    0.0  1.0  NaN  NaN
two    0.0  1.0  NaN  NaN
three  NaN  NaN  5.0  6.0


In [339]: pd.concat([s1,s2,s3],axis=1, keys=['one', 'two', 'three'])
Out[339]:
   one  two  three
a  0.0  NaN    NaN
b  1.0  NaN    NaN
c  NaN  2.0    NaN
d  NaN  3.0    NaN
e  NaN  4.0    NaN
f  NaN  NaN    5.0
g  NaN  NaN    6.0

df1 = DataFrame(np.arange(6).reshape((3,2)), index=['a', 'b', 'c'], columns=['one', 'two'])

df2 = DataFrame(5 + np.arange(4).reshape((2,2)), index=['a', 'c'], columns=['three', 'four'])

pd.concat([df1,df2], axis=1, keys=['level1', 'level2'])
Out[340]:
  level1     level2
     one two  three four
a      0   1    5.0  6.0
b      2   3    NaN  NaN
c      4   5    7.0  8.0

df1 = DataFrame(np.random.randn(3,4), columns=['a', 'b', 'c', 'd'])

df2 = DataFrame(np.random.randn(2,3), columns=['b', 'd', 'e'])

In [341]: pd.concat([df1,df2], axis=1, keys=['level1', 'level2'], names=['upper'
     ...: ,'lower'])
Out[341]:
upper level1     level2
lower    one two  three four
a          0   1    5.0  6.0
b          2   3    NaN  NaN
c          4   5    7.0  8.0

In [342]: ^M
     ...: df2 = DataFrame(np.random.randn(2,3), columns=['b', 'd', 'e'])

In [343]: ^M
     ...: df1 = DataFrame(np.random.randn(3,4), columns=['a', 'b', 'c', 'd'])^M
     ...:

In [344]: pd.concat([df1, df2], ignore_index = True)
Out[344]:
          a         b         c         d         e
0 -0.149109  1.938157 -0.288789  0.365936       NaN
1 -0.364722  0.012950 -0.205709  0.070271       NaN
2 -0.212040  0.266300  0.570376  1.123322       NaN
3       NaN  0.331917       NaN  1.457976  0.453139
4       NaN -0.283265       NaN -2.491352  1.359737


#####$$合并重叠数据$$#####

a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan], index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a)), dtype=np.float64, index=['f', 'e', 'd', 'c', 'b', 'a'])

In [346]: np.where(pd.isnull(a), b,a)
Out[346]: array([0. , 2.5, 2. , 3.5, 4.5, 5. ])

In [351]: b[:-2].combine_first(a[2:])
Out[351]:
a    NaN
b    4.5
c    3.0
d    2.0
e    1.0
f    0.0
dtype: float64

df1 = DataFrame({'a':[1.,np.nan,5.,np.nan],
'b':[np.nan, 2, np.nan, 6],
'c':range(2,18,4)
})

df2 = DataFrame(
{'a':[5.,4.,np.nan,3.,7.],
'b':[np.nan, 3., 4., 6., 8.]
})

In [353]: df1.combine_first(df2)
Out[353]:
     a    b     c
0  1.0  NaN   2.0
1  4.0  2.0   6.0
2  5.0  4.0  10.0
3  3.0  6.0  14.0
4  7.0  8.0   NaN

#####$$重塑和轴向旋转$$#####

data = DataFrame(np.arange(6).reshape((2,3)), index = pd.Index(['Ohio', 'Colorado'], name='state'), columns=pd.Index(['one', 'two', 'three'], name = 'number'))

In [357]: result = data.stack()

In [358]: result
Out[358]:
state     number
Ohio      one       0
          two       1
          three     2
Colorado  one       3
          two       4
          three     5
dtype: int32

In [359]: result.unstack()
Out[359]:
number    one  two  three
state
Ohio        0    1      2
Colorado    3    4      5

In [360]: result.unstack(0)
Out[360]:
state   Ohio  Colorado
number
one        0         3
two        1         4
three      2         5

In [361]: result.unstack('state')
Out[361]:
state   Ohio  Colorado
number
one        0         3
two        1         4
three      2         5

s1 = Series([0,1,2,3],index=['a', 'b', 'c', 'd'])
s2 = Series([4,5,6], index=['c', 'd', 'e'])
data2 = pd.concat([s1,s2], keys=['one', 'two'])

data2.unstack()

In [366]: data2.unstack()
Out[366]:
       a    b    c    d    e
one  0.0  1.0  2.0  3.0  NaN
two  NaN  NaN  4.0  5.0  6.0

df = DataFrame({'left':result, 'right':result+5}, columns=pd.Index(['left', 'right'], name = 'side'))

In [371]: df.unstack('state')
Out[371]:
side   left          right
state  Ohio Colorado  Ohio Colorado
number
one       0        3     5        8
two       1        4     6        9
three     2        5     7       10


#在对DataFrame进行unstack操作时，作为旋转轴的层将会成为结果中最低的层
In [372]: df.unstack('state').stack('side')
Out[372]:
state         Colorado  Ohio
number side
one    left          3     0
       right         8     5
two    left          4     1
       right         9     6
three  left          5     2
       right        10     7
	   
#####$$将“长格式”旋转为“宽格式”$$#####

data = pd.read_csv('C:\Users\Administrator\learngit\ch07\macrodata.csv')

In [371]: df.unstack('state')
Out[371]:
side   left          right
state  Ohio Colorado  Ohio Colorado
number
one       0        3     5        8
two       1        4     6        9
three     2        5     7       10

In [372]: df.unstack('state').stack('side')
Out[372]:
state         Colorado  Ohio
number side
one    left          3     0
       right         8     5
two    left          4     1
       right         9     6
three  left          5     2
       right        10     7

In [373]:data = pd.read_csv('C:\Users\Administrator\learngit\ch07\macrodata.csv')
	 
In [376]: periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='d
     ...: ate')

In [377]: periods
Out[377]:
PeriodIndex(['1959Q1', '1959Q2', '1959Q3', '1959Q4', '1960Q1', '1960Q2',
             '1960Q3', '1960Q4', '1961Q1', '1961Q2',
             ...
             '2007Q2', '2007Q3', '2007Q4', '2008Q1', '2008Q2', '2008Q3',
             '2008Q4', '2009Q1', '2009Q2', '2009Q3'],
            dtype='period[Q-DEC]', name=u'date', length=203, freq='Q-DEC')

In [378]: data=DataFrame(data.to_records(), columns=pd.Index(['realgdp', 'infl',
     ...: 'unemp'], name =  'item'), index=periods.to_timestamp('D', 'end'))
	 
In [380]: ldata = data.stack().reset_index().rename(columns={0:'values'})

In [385]: pivoted = ldata.pivot('date', 'item', 'values')

In [386]: pivoted.head()
Out[386]:
item        infl   realgdp  unemp
date
1959-03-31  0.00  2710.349    5.8
1959-06-30  2.34  2778.801    5.1
1959-09-30  2.74  2775.488    5.3
1959-12-31  0.27  2785.204    5.6
1960-03-31  2.31  2847.699    5.2



In [381]: ldata[:10]
Out[381]:
        date     item    values
0 1959-03-31  realgdp  2710.349
1 1959-03-31     infl     0.000
2 1959-03-31    unemp     5.800
3 1959-06-30  realgdp  2778.801
4 1959-06-30     infl     2.340
5 1959-06-30    unemp     5.100
6 1959-09-30  realgdp  2775.488
7 1959-09-30     infl     2.740
8 1959-09-30    unemp     5.300
9 1959-12-31  realgdp  2785.204

In [388]: ldata['value2'] = np.random.randn(len(ldata))

In [389]: ldata.head()
Out[389]:
        date     item    values    value2
0 1959-03-31  realgdp  2710.349  1.265828
1 1959-03-31     infl     0.000  2.301270
2 1959-03-31    unemp     5.800 -1.610212
3 1959-06-30  realgdp  2778.801 -0.228562
4 1959-06-30     infl     2.340 -0.431444

In [390]: ldata.head(10)
Out[390]:
        date     item    values    value2
0 1959-03-31  realgdp  2710.349  1.265828
1 1959-03-31     infl     0.000  2.301270
2 1959-03-31    unemp     5.800 -1.610212
3 1959-06-30  realgdp  2778.801 -0.228562
4 1959-06-30     infl     2.340 -0.431444
5 1959-06-30    unemp     5.100  0.536569
6 1959-09-30  realgdp  2775.488 -0.319271
7 1959-09-30     infl     2.740  0.403021
8 1959-09-30    unemp     5.300  0.111870
9 1959-12-31  realgdp  2785.204  0.083719

In [391]: pivoted = ldata.pivot('date', 'item')

In [392]: pivoted.head()
Out[392]:
           values                    value2
item         infl   realgdp unemp      infl   realgdp     unemp
date
1959-03-31   0.00  2710.349   5.8  2.301270  1.265828 -1.610212
1959-06-30   2.34  2778.801   5.1 -0.431444 -0.228562  0.536569
1959-09-30   2.74  2775.488   5.3  0.403021 -0.319271  0.111870
1959-12-31   0.27  2785.204   5.6  0.097532  0.083719  1.249430
1960-03-31   2.31  2847.699   5.2  1.780917  0.217617  1.214845

In [395]: pivoted['values'].head()
Out[395]:
item        infl   realgdp  unemp
date
1959-03-31  0.00  2710.349    5.8
1959-06-30  2.34  2778.801    5.1
1959-09-30  2.74  2775.488    5.3
1959-12-31  0.27  2785.204    5.6
1960-03-31  2.31  2847.699    5.2

#####$$移除重复数据$$#####

data = DataFrame({'k1': ['one'] * 3 + ['two']*4,
'k2':[1,1,2,3,3,4,4]
})


In [398]: data
Out[398]:
    k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4

In [399]: data.duplicated()
Out[399]:
0    False
1     True
2    False
3    False
4     True
5    False
6     True
dtype: bool

In [404]: data.drop_duplicates()
Out[404]:
    k1  k2
0  one   1
2  one   2
3  two   3
5  two   4

In [406]: data.drop_duplicates(['k1'])
Out[406]:
    k1  k2  v1
0  one   1   0
3  two   3   3

#保留最后一个重复项
In [409]: data.drop_duplicates(['k1'], keep = 'last')
Out[409]:
    k1  k2  v1
2  one   2   2
6  two   4   6

#####$$利用函数或映射进行数据转换$$#####

data = DataFrame({'food':['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
'ounces' : [4,3,12,6,7.5,8,3,5,6]
})

meat_to_animal = {
'bacon' : 'pig',
'pulled pork' : 'pig',
'pastrami' : 'cow',
'corned beef' : 'cow',
'honey ham': 'pig',
'nova lox' : 'salmon'
}

In [420]: data['food'].map(str.lower).map(meat_to_animal)
Out[420]:
0       pig
1       pig
2       pig
3       cow
4       cow
5       pig
6       cow
7       pig
8    salmon
Name: food, dtype: object


In [422]: data['food'].map(lambda x : meat_to_animal[x.lower()])
Out[422]:
0       pig
1       pig
2       pig
3       cow
4       cow
5       pig
6       cow
7       pig
8    salmon
Name: food, dtype: object


In [423]: data = Series([1, -999., -2, -999.,-1000., 3])

In [424]: data
Out[424]:
0       1.0
1    -999.0
2      -2.0
3    -999.0
4   -1000.0
5       3.0
dtype: float64

#####$$替换值$$#####

In [423]: data = Series([1, -999., -2, -999.,-1000., 3])

In [424]: data
Out[424]:
0       1.0
1    -999.0
2      -2.0
3    -999.0
4   -1000.0
5       3.0
dtype: float64

In [429]: data.replace([-999., -1000.], np.nan)
Out[429]:
0    1.0
1    NaN
2   -2.0
3    NaN
4    NaN
5    3.0
dtype: float64

#####$$重命名轴索引$$#####
data = DataFrame(np.arange(12).reshape((3,4)), index = ['Ohio', 'Colorado', 'New York'], columns = ['one', 'two', 'three', 'four'])

In [432]: data.index.map(str.upper)
Out[432]: Index([u'OHIO', u'COLORADO', u'NEW YORK'], dtype='object')

In [433]: data.index = data.index.map(str.upper)

In [434]: data
Out[434]:
          one  two  three  four
OHIO        0    1      2     3
COLORADO    4    5      6     7
NEW YORK    8    9     10    11

In [435]: data.rename(index = str.title, columns=str.upper)
Out[435]:
          ONE  TWO  THREE  FOUR
Ohio        0    1      2     3
Colorado    4    5      6     7
New York    8    9     10    11

data.rename(index={'OHIO':'INDIANA'}, columns={'three':'peekaboo'})


In [436]: data.rename(index={'OHIO':'INDIANA'}, columns={'three':'peekaboo'})
Out[436]:
          one  two  peekaboo  four
INDIANA     0    1         2     3
COLORADO    4    5         6     7
NEW YORK    8    9        10    11


_ = data.rename(index={'OHIO':'INDIANA'}, inplace=True)


In [437]: _ = data.rename(index={'OHIO':'INDIANA'}, inplace=True)

In [438]: data
Out[438]:
          one  two  three  four
INDIANA     0    1      2     3
COLORADO    4    5      6     7
NEW YORK    8    9     10    11

#####$$离散化和面元划分$$#####

In [439]: ages = [20,22,25,27,21,23,37,61,45,41,32]

In [440]: ages
Out[440]: [20, 22, 25, 27, 21, 23, 37, 61, 45, 41, 32]

bins = [18,25,35,60,100]

cats = pd.cut(ages, bins)

In [441]: bins = [18,25,35,60,100]
     ...:
     ...: cats = pd.cut(ages, bins)
     ...:

In [442]: cats
Out[442]:
[(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (35, 60], (60, 100], (35, 60], (35, 60], (25, 35]]
Length: 11
Categories (4, interval[int64]): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]


In [444]: cats.codes
Out[444]: array([0, 0, 0, 1, 0, 0, 2, 3, 2, 2, 1], dtype=int8)

In [448]: cats.categories
Out[448]:
IntervalIndex([(18, 25], (25, 35], (35, 60], (60, 100]]
              closed='right',
              dtype='interval[int64]')
			  
In [449]: cats.value_counts()
Out[449]:
(18, 25]     5
(25, 35]     2
(35, 60]     3
(60, 100]    1
dtype: int64

In [450]: pd.cut(ages, [18,26,36,61,100], right = False)
Out[450]:
[[18, 26), [18, 26), [18, 26), [26, 36), [18, 26), ..., [36, 61), [61, 100), [36, 61), [36, 61), [26, 36)]
Length: 11
Categories (4, interval[int64]): [[18, 26) < [26, 36) < [36, 61) < [61, 100)]

group_names = ['Youth', 'YouthAdult', 'MiddleAged', 'Senior']

pd.cut(ages, bins, labels=group_names)

In [452]: group_names = ['Youth', 'YouthAdult', 'MiddleAged', 'Senior']^M
     ...: ^M
     ...: pd.cut(ages, bins, labels=group_names)
     ...:
Out[452]:
[Youth, Youth, Youth, YouthAdult, Youth, ..., MiddleAged, Senior, MiddleAged, MiddleAged, YouthAdult]
Length: 11
Categories (4, object): [Youth < YouthAdult < MiddleAged < Senior]


In [453]: data = np.random.rand(20)

In [454]: pd.cut(data, 4, precision =2)
Out[454]:
[(0.47, 0.7], (0.25, 0.47], (0.7, 0.92], (0.031, 0.25], (0.031, 0.25], ..., (0.031, 0.25], (0.25, 0.47], (0.031, 0.25],
(0.47, 0.7], (0.031, 0.25]]
Length: 20
Categories (4, interval[float64]): [(0.031, 0.25] < (0.25, 0.47] < (0.47, 0.7] < (0.7, 0.92]]


#按百分位数进行分箱操作
In [456]: data = np.random.randn(1000)

In [457]: pd.qcut(data, 4)
Out[457]:
[(-3.655, -0.615], (-0.615, -0.0112], (-0.615, -0.0112], (0.663, 3.314], (-3.655, -0.615], ..., (-0.0112, 0.663], (0.663
, 3.314], (-0.615, -0.0112], (-3.655, -0.615], (-0.615, -0.0112]]
Length: 1000
Categories (4, interval[float64]): [(-3.655, -0.615] < (-0.615, -0.0112] < (-0.0112, 0.663] <
                                    (0.663, 3.314]]
									
									

In [462]: pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.0])
Out[462]:
[(-1.199, -0.0112], (-1.199, -0.0112], (-1.199, -0.0112], (-0.0112, 1.283], (-1.199, -0.0112], ..., (-0.0112, 1.283], (1
.283, 3.314], (-1.199, -0.0112], (-3.655, -1.199], (-1.199, -0.0112]]
Length: 1000
Categories (4, interval[float64]): [(-3.655, -1.199] < (-1.199, -0.0112] < (-0.0112, 1.283] <
                                    (1.283, 3.314]]

									
#####$$检测和过滤异常值$$#####	

In [467]: np.random.seed(12345)

In [468]: data = DataFrame(np.random.randn(1000,4))

In [473]: col[np.abs(col) > 3]
Out[473]:
97     3.927528
305   -3.399312
400   -3.745356
Name: 3, dtype: float64

In [474]: data[(np.abs(data) > 3).any(1)]
Out[474]:
            0         1         2         3
5   -0.539741  0.476985  3.248944 -1.021228
97  -0.774363  0.552936  0.106061  3.927528
102 -0.655054 -0.565230  3.176873  0.959533
305 -2.315555  0.457246 -0.025907 -3.399312
324  0.050188  1.951312  3.260383  0.963301
400  0.146326  0.508391 -0.196713 -3.745356
499 -0.293333 -0.242459 -3.056990  1.918403
523 -3.428254 -0.296336 -0.439938 -0.867165
586  0.275144  1.179227 -3.184377  1.369891
808 -0.362528 -3.548824  1.553205 -2.186301
900  3.366626 -2.372214  0.851010  1.332846

In [475]: data[np.abs(data) > 3] = np.sign(data) * 3

In [476]: data.describe()
Out[476]:
                 0            1            2            3
count  1000.000000  1000.000000  1000.000000  1000.000000
mean     -0.067623     0.068473     0.025153    -0.002081
std       0.995485     0.990253     1.003977     0.989736
min      -3.000000    -3.000000    -3.000000    -3.000000
25%      -0.774890    -0.591841    -0.641675    -0.644144
50%      -0.116401     0.101143     0.002073    -0.013611
75%       0.616366     0.780282     0.680391     0.654328
max       3.000000     2.653656     3.000000     3.000000

#####$$排列和随机采样$$#####
In [477]: df = DataFrame(np.arange(5*4).reshape(5,4))

In [478]: sampler = np.random.permutation(5)

In [481]: sampler
Out[481]: array([1, 3, 4, 0, 2])


In [499]: bag = np.array([5,7,-1,6,4])

In [500]: sampler = np.random.randint(0, len(bag), size=10)

In [501]: sampler
Out[501]: array([0, 4, 4, 4, 3, 4, 2, 2, 4, 3])

In [502]: draws = bag.take(sampler)

In [503]: draws
Out[503]: array([ 5,  4,  4,  4,  6,  4, -1, -1,  4,  6])


#####$$计算指标/哑变量$$#####

df = DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'b'],
'data1' : range(6)
})


from pandas import Series
import numpy as np
import pandas as pd

pd.get_dummies(df['key'])
[]
dummies = pd.get_dummies(df['key'], prefix='key')

df_with_dummy = df[['data1']].join(dummies)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table("C:\\Users\\Administrator\\learngit\\ch02\\movies.dat",sep='::', header=None, names=mnames)

genre_iter = (set(x.split('|')) for x in movies.genres)			#产生generator类型的变量
genres = sorted(set.union(*genre_iter))							#将generator中的每个元素执行set.union操作


genre_iter1 = [set(x.split('|')) for x in movies.genres]
genres = set()

for x in genre_iter:
	genres= genres.union(x)

dummies = DataFrame(np.zeros((len(movies), len(genres))), columns=genres)


movies_windic = movies.join(dummies.add_prefix('Genre_'))

values = np.random.rand(10)

values

bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

pd.get_dummies(pd.cut(values, bins))

#####$$字符串操作$$#####

val = 'a,b, guido'
val.split(',')

pieces = [x.strip for x in val.split(',')]

pieces

'::'.join(pieces)

#####$$正则表达式$$#####
import re
text = "foo		bar\t baz		\tqux"

re.split('\s+', text)

regex = re.compile('\s+')

regex.split(text)
regex.findall(text)

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'


regex = re.compile(pattern, flags=re.IGNORECASE)