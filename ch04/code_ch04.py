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


