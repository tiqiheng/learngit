In [97]: !type C:\Users\Administrator\learngit\ch06\ex1.csv
a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo

In [98]: df = pd.read_csv('C:\Users\Administrator\learngit\ch06\ex1.csv')

In [99]: df
Out[99]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo

In [100]: pd.read_table('C:\Users\Administrator\learngit\ch06\ex1.csv', sep=',')
Out[100]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo

In [101]: pd
Out[101]: <module 'pandas' from 'd:\python27\lib\site-packages\pandas\__init__.pyc'>

In [102]: !type C:\Users\Administrator\learngit\ch06\ex2.csv
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
In [103]: pd.read_csv('C:\Users\Administrator\learngit\ch06\ex2.csv', header = None)
Out[103]:
   0   1   2   3      4
0  1   2   3   4  hello
1  5   6   7   8  world
2  9  10  11  12    foo

In [104]: pd.read_csv('C:\Users\Administrator\learngit\ch06\ex2.csv', names = ['a', 'b', 'c', 'd', 'message'])
Out[104]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo


names = ['a', 'b', 'c', 'd', 'message']

In [106]: pd.read_csv('C:\Users\Administrator\learngit\ch06\ex2.csv', names = names, index_col ='message')
Out[106]:
         a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12


In [112]: list(open('C:\Users\Administrator\learngit\ch06\ex3.txt'))
Out[112]:
['            A         B         C\n',
 'aaa -0.264438 -1.026059 -0.619500\n',
 'bbb  0.927272  0.302904 -0.032399\n',
 'ccc -0.264273 -0.386314 -0.217601\n',
 'ddd -0.871858 -0.348382  1.100491\n']

 
In [116]: !type C:\Users\Administrator\learngit\ch06\ex4.csv
# hey!
a,b,c,d,message
# just wanted to make things more difficult for you
# who reads CSV files with computers, anyway?
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
 
In [121]: result = pd.read_csv('C:\Users\Administrator\learngit\ch06\ex4.csv',sk
     ...: iprows=[0,2,3])

In [122]: result
Out[122]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo

In [123]: !type C:\Users\Administrator\learngit\ch06\ex5.csv
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo

In [124]: result = pd.read_csv('C:\Users\Administrator\learngit\ch06\ex5.csv')

In [125]: result
Out[125]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo


In [126]: pd.isnull(result)
Out[126]:
   something      a      b      c      d  message
0      False  False  False  False  False     True
1      False  False  False   True  False    False
2      False  False  False  False  False    False

In [127]: result = pd.read_csv('C:\Users\Administrator\learngit\ch06\ex5.csv',na_values=['NULL'])

In [128]: result
Out[128]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo


In [129]: sentinels = {'message':['foo'], 'something' : ['two']}

In [130]: pd.read_csv('C:\Users\Administrator\learngit\ch06\ex5.csv',na_values=sentinels)
Out[130]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       NaN  5   6   NaN   8   world
2     three  9  10  11.0  12     NaN


In [135]: pd.read_csv('C:\Users\Administrator\learngit\ch06\ex5.csv', nrows = 5)
     ...:
Out[135]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo

In [137]: chunker = pd.read_csv('C:\Users\Administrator\learngit\ch06\ex6.csv',chunksize = 1000)

In [138]: chunker
Out[138]: <pandas.io.parsers.TextFileReader at 0x5e31e30>

chunker = pd.read_csv('C:\Users\Administrator\learngit\ch06\ex6.csv',chunksize = 1000)

tot = Series([])

for piece in chunker:
	tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending = False)


#####$$将数据写到文本格式$$#####

In [149]: data = pd.read_csv('C:\Users\Administrator\learngit\ch06\ex5.csv')

In [150]: data
Out[150]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo

In [151]: data.to_csv('C:\Users\Administrator\learngit\ch06\out.csv')

In [152]: !type C:\Users\Administrator\learngit\ch06\out.csv
,something,a,b,c,d,message
0,one,1,2,3.0,4,
1,two,5,6,,8,world
2,three,9,10,11.0,12,foo

In [154]: import sys

In [155]: data.to_csv(sys.stdout,sep='|')
|something|a|b|c|d|message
0|one|1|2|3.0|4|
1|two|5|6||8|world
2|three|9|10|11.0|12|foo

In [157]: data.to_csv(sys.stdout,na_rep = 'NULL')
,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo

In [157]: data.to_csv(sys.stdout,na_rep = 'NULL')
,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo

In [158]: data.to_csv(sys.stdout,index=False, header=False)
one,1,2,3.0,4,
two,5,6,,8,world
three,9,10,11.0,12,foo

In [161]: data.to_csv(sys.stdout,index=False, columns=['a','b','c'])
a,b,c
1,2,3.0
5,6,
9,10,11.0

In [162]: datas = pd.date_range('1/1/2000', periods = 7)

In [164]: ts = Series(np.arange(7), index=datas)

In [165]: ts
Out[165]:
2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
2000-01-06    5
2000-01-07    6
Freq: D, dtype: int32

In [185]: !type C:\Users\Administrator\learngit\ch06\ex7.csv
"a","b","c"
"1","2","3"
"1","2","3"

In [186]: import csv

In [187]: f = open('C:\Users\Administrator\learngit\ch06\ex7.csv')

In [188]: reader = csv.reader(f)

for line in reader:
	print line

lines = list(csv.reader(open('C:\Users\Administrator\learngit\ch06\ex7.csv'))

header, values = lines[0], lines[1:]

data_dict = {h:v for h, v in zip(header,zip(*values))}

class my_dialect(csv.Dialect):
	lineterminator = '\n'
	delimiter = ';'
	quotechar = '"'
	quoting = 0
	
	
reader = csv.reader(f,dialect=my_dialect)

with open('C:\Users\Administrator\learngit\ch06\\mydata.csv', 'w') as f:
	writer = csv.writer(f, dialect = my_dialect)
	writer.writerow(('one', 'two', 'three'))
	writer.writerow(('1', '2', '3'))
	writer.writerow(('4', '5', '6'))
	writer.writerow(('7', '8', '9'))
	
In [227]: !type C:\Users\Administrator\learngit\ch06\\mydata.csv
one;two;three
1;2;3
4;5;6
7;8;9

