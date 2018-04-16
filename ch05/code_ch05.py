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
