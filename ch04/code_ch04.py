########################################################
#####                 第四章                     #######
########################################################

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr1 = np.array(data2)

#获取ndarray的维度
arr1.ndim

#获取ndarray的结构
arr1.shape

np.zeros(10)

np.zeros((3,6))


#未初始化的垃圾值，尽量不用
np.empty((2,3,2))

np.zeros_like(arr1)

np.identity(3)

#使用dtype限制数据的类型
arr1 = np.array([1,2,3], dtype=np.float64)

arr2 = np.array([1,2,3], dtype=np.int32)

#使用astype修改数据类型
arr = np.array([1,2,3,4,5])

arr.dtype

float_arr = arr.astype(np.float64)
float_arr.dtype

#整数转换为浮点数将全部被截断
arr = np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
arr.astype(np.int32)

#如果字符串数组表示的全是数字，也可以用astype将其转换为数值形式
numric_strings = np.array(['1.25','-9.6','42'],dtype=np.string_)

numric_strings.astype(np.float64)

#dtype的其他用法
int_array = np.arange(10)
calibers = np.array([.22,.270,.357,.380,.44,.50],dtype=np.float64)
int_array.astype(calibers.dtype)

empty_uint32 = np.empty(8,dtype='u4')

#数组与标量之间的运算（广播）
arr = np.array([[1.,2.,3.],[4.,5.,6.]])

1/arr


#索引和切片
arr = np.arange(10)

arr[5] arr[5:8]

arr[5:8]=12

#数据不会被复制，视图上的任何修改都会直接反映到源数组上
arr_slice = arr[5:8]

arr_slice[1] = 12345

#二维ndarray的索引
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2d[0][2] arr2d[0,2]

#布尔型数组
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])

data =randn(7,4)
names=='Bob'

data[names=='Bob']

#布尔运算

mask = (names=='Bob') | (names=='Will')
data[mask]

#花式索引
arr = np.empty((8,4))

for i in range(8):
	arr[i] = i
	
arr[[4,3,0,6]]

arr[[-3,-5, -1]] #使用负数将从后面开始索引

arr = np.arange(32).reshape((8,4))


arr[[1,5,7,2],[0,3,1,2]]


arr[[1,5,7,2]][[0,3,1,2]]

arr[np.ix_([1,5,7,2],[0,3,1,2])]

arr.T #进行数组转置


points = np.arange(-5,5,0.01)

xs, ys = np.meshgrid(points, points)

import matplotlib.pyplot as plt

z = np.sqrt(xs**2 + ys**2)

z

plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()

plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")

#####$$将条件逻辑表述为数组运算$$#####

xarr = np.array([1.1,1.2,1.3,1.4,1.5])

yarr = np.array([2.1,2.2,2.3,2.4,2.5])

cond = np.array([True, False, True, True, False])

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]

result = np.where(cond, xarr, yarr)


result = np.where(xarr >= 1.3, 2, 1)


arr = randn(4)

np.where(arr > 0, 2, -2)

np.where(arr>0, 2, arr)


np.where(cond1 & cond2, 0, np.where(cond1, 1, np.where(cond2, 2,3)))

result = []
for i in range(n):
	if cond1[i] and cond2[i]:
		result.append(0)
	elif cond1[i]:
		result.append(1)
	elif cond2[i]:
		result.append(2)
	else:
		result.append(3)
		

#####$$数学和统计方法$$#####
arr = np.random.randn(5,4)    #正态分布的数据
arr.mean()
np.random.randn(5,4)

np.mean(arr)

arr.sum()


arr.mean(axis=1)
arr.sum(0)

arr = np.arange(0,9).reshape(3,3)

arr = randn(100)

(arr > 0).sum()

bools = np.array([True, False, True, True, False])

bools.any() #用于检查数组中是否有一个或多个True

bools.all() #用于检查数组中所有值是否都是True

arr = randn(8)

arr.sort()

arr = randn(5,3)

arr.sort(1)

large_arr = randn(1000)

large_arr.sort()

large_arr[int(0.05*len(large_arr))]

step = np.arange(0,1,0.05)

large_arr[int(1000*step)]

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

np.unique(names)


ints = np.array([3,3,3,2,2,1,1,4,4])
np.unique(ints)


values = np.array([6,0,0,3,2,5,6])
np.in1d(values, [2,3,6])


#####$$将数组以二进制格式保存磁盘$$#####

arr = np.arange(10)

np.save('some_array', arr)

np.load('some_array.npy')

np.savez('array_archive.npz', a=arr, b=arr)

arch = np.load('array_archive.npz')
arch['b']
