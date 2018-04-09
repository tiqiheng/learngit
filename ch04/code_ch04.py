########################################################
#####                 ������                     #######
########################################################

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr1 = np.array(data2)

#��ȡndarray��ά��
arr1.ndim

#��ȡndarray�Ľṹ
arr1.shape

np.zeros(10)

np.zeros((3,6))


#δ��ʼ��������ֵ����������
np.empty((2,3,2))

np.zeros_like(arr1)

np.identity(3)

#ʹ��dtype�������ݵ�����
arr1 = np.array([1,2,3], dtype=np.float64)

arr2 = np.array([1,2,3], dtype=np.int32)

#ʹ��astype�޸���������
arr = np.array([1,2,3,4,5])

arr.dtype

float_arr = arr.astype(np.float64)
float_arr.dtype

#����ת��Ϊ��������ȫ�����ض�
arr = np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
arr.astype(np.int32)

#����ַ��������ʾ��ȫ�����֣�Ҳ������astype����ת��Ϊ��ֵ��ʽ
numric_strings = np.array(['1.25','-9.6','42'],dtype=np.string_)

numric_strings.astype(np.float64)

#dtype�������÷�
int_array = np.arange(10)
calibers = np.array([.22,.270,.357,.380,.44,.50],dtype=np.float64)
int_array.astype(calibers.dtype)

empty_uint32 = np.empty(8,dtype='u4')

#���������֮������㣨�㲥��
arr = np.array([[1.,2.,3.],[4.,5.,6.]])

1/arr


#��������Ƭ
arr = np.arange(10)

arr[5] arr[5:8]

arr[5:8]=12

#���ݲ��ᱻ���ƣ���ͼ�ϵ��κ��޸Ķ���ֱ�ӷ�ӳ��Դ������
arr_slice = arr[5:8]

arr_slice[1] = 12345

#��άndarray������
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2d[0][2] arr2d[0,2]

#����������
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])

data =randn(7,4)
names=='Bob'

data[names=='Bob']

#��������

mask = (names=='Bob') | (names=='Will')
data[mask]

#��ʽ����
arr = np.empty((8,4))

for i in range(8):
	arr[i] = i
	
arr[[4,3,0,6]]

arr[[-3,-5, -1]] #ʹ�ø������Ӻ��濪ʼ����

arr = np.arange(32).reshape((8,4))


arr[[1,5,7,2],[0,3,1,2]]


arr[[1,5,7,2]][[0,3,1,2]]

arr[np.ix_([1,5,7,2],[0,3,1,2])]

arr.T #��������ת��


points = np.arange(-5,5,0.01)

xs, ys = np.meshgrid(points, points)

import matplotlib.pyplot as plt

z = np.sqrt(xs**2 + ys**2)

z

plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()

plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")

#####$$�������߼�����Ϊ��������$$#####

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
		

#####$$��ѧ��ͳ�Ʒ���$$#####
arr = np.random.randn(5,4)    #��̬�ֲ�������
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

bools.any() #���ڼ���������Ƿ���һ������True

bools.all() #���ڼ������������ֵ�Ƿ���True

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


#####$$�������Զ����Ƹ�ʽ�������$$#####

arr = np.arange(10)

np.save('some_array', arr)

np.load('some_array.npy')

np.savez('array_archive.npz', a=arr, b=arr)

arch = np.load('array_archive.npz')
arch['b']
