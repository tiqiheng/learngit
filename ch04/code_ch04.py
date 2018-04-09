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


