#coding = utf-8


path = 'F:\OutJob_tiqh\DataAnalysisWithPython\ch02\usa_gov_bitly_data.txt'

open(path).readline()

import json

path = 'F:\OutJob_tiqh\DataAnalysisWithPython\ch02\usa_gov_bitly_data.txt'

records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

time_zones[:10]

def get_counts(sequence):
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts
	
from collections import defaultdict

def get_counts2(sequence):
	counts = defaultdict(int) #所有的值均被初始化为0
	for x in sequence:
		counts[x] += 1
	return counts
	
def top_counts(count_dict, n=10):
	value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:]

#元组的排序可以通过如下方式选择键值
#sorted(mylist, key = lamda x : (x[0],x[1]), reverse = True)

from collections import Counter

counts = Counter(time_zones)

counts.most_common(10)

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

frame = DataFrame(records)

frame['tz'][:10]

tz_counts = frame['tz'].value_counts()
tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()

tz_counts[:10]

tz_counts[:10].plot('barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])

results[:5]

results.value_counts()[:8]

cframe = frame[frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)
#unstack 的作用？

indexer = agg_counts.sum(1).argsort()

indexer[:10]

count_subset = agg_counts.take(indexer)[-10:]

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']

users = pd.read_table('F:\OutJob_tiqh\DataAnalysisWithPython\ch02\users.dat', sep = '::', header=None, names=unames, engine = 'python') #此处加入engine='python' 目的为避免警告：ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']

ratings = pd.read_table('F:\OutJob_tiqh\DataAnalysisWithPython\ch02\\ratings.dat', sep = '::', header=None, names=rnames, engine = 'python')#注意由于反斜杠是转义字符，所以作为文件名，应尽量

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('F:\OutJob_tiqh\DataAnalysisWithPython\ch02\movies.dat', sep = '::', header=None, names=mnames, engine = 'python')

data = pd.merge(pd.merge(ratings, users), movies)

data.ix[0]

mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
#上面的代码会报错，需要将rows代替为index，cols替换为columns

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

mean_ratings[:5]

ratings_by_title = data.groupby('title').size()

ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles

mean_ratings = mean_ratings.ix[active_titles]
#D:\Python27\Scripts\ipython:1: DeprecationWarning:
# .ix is deprecated. Please use
# .loc for label based indexing or
# .iloc for positional indexing
mean_ratings = mean_ratings.loc[active_titles]

mean_ratings

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_values(by='diff')

sorted_by_diff[:15]

sorted_by_diff[::-1][:15]

rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.loc[active_titles]
rating_std_by_title.sort_values(ascending=False)[:10]



############################################################
#######                 第三小节                     #######
############################################################
names1880 = pd.read_csv('F:\\OutJob_tiqh\\DataAnalysisWithPython\\ch02\\babynames\\yob1880.txt', names = ['name', 'sex', 'births'])

names1880.groupby('sex').births.sum()

years = range(1880, 2011)

pieces = []

columns = ['name', 'sex', 'births' ]

for year in years:
	path = "F:/OutJob_tiqh/DataAnalysisWithPython/ch02/babynames/yob%02d.txt" % year
	frame = pd.read_csv(path, names = columns)
	
	frame['year'] = year
	pieces.append(frame)

names = pd.concat(pieces, ignore_index = True)

total_births = names.pivot_table('births', index = 'year', columns = 'sex', aggfunc = 'sum')

total_births.tail()

total_births.plot(title = 'Total births group by year and sex')

def add_prop(group):
	#整数除法会向下园整
	births = group.births.astype(float)
	
	group['prop'] = births/births.sum()
	return group
	
names = names.groupby(['year', 'sex']).apply(add_prop)

np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

def get_top1000(group):
	return group.sort_index(by='births', ascending=False)[:1000]

grouped = names.groupby(['year', 'sex'])

top1000 = grouped.apply(get_top1000)
	
pieces = []

for year, group in names.groupby(['year', 'sex']):
	pieces.append(group.sort_values(by='births', ascending=False)[:1000])
	
top1000 = pd.concat(pieces, ignore_index = True)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index = 'year', columns = 'name', aggfunc = sum)

subset = total_births[['John','Harry','Mary','Marilyn']]

subset.plot(subplots=True, figsize=(12,10), grid=False, title="Number of births per year")

table = top1000.pivot_table('prop', index = 'year', columns = 'sex', aggfunc = sum)

table.plot(title = 'Sum of top1000.prop by year and sex', yticks=np.linspace(0,1.2,13), xticks=range(1880,2020,10))

df = boys[boys.year == 2010]

prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()

prop_cumsum[:10]

def get_quantile_count(group, q=0.5):
	group = group.sort_values(by='prop', ascending=False)
	#you now have to call `.values` to return a ndarray I believe this is due to the refactoring that occurred in Pandas 0.13.0 where Pandas Series now sub-class NDFrame rather than ndarray
	return group.prop.values.cumsum().searchsorted(q) + 1
	
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

diversity.plot(title = 'Number of popular names in top 50%')

#从name列取出最后一个字母
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table('births', index = last_letters, columns = ['sex', 'year'], aggfunc = sum)

subtable = table.reindex(columns=[1910,1960,2010], level='year')

letter_prop = subtable / subtable.sum().astype(float)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,1,figsize=(10,8))
letter_prop['M'].plot(kind='bar', rot =0, ax =axes[0], title = 'Male')
letter_prop['F'].plot(kind='bar', rot =0, ax =axes[1], title = 'Feale', legend = False)

letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.loc[['d', 'n', 'y'], 'M'].T

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]

filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()

table = filtered.pivot_table('births', index = 'year', columns = 'sex', aggfunc = sum)

table = table.div(table.sum(1), axis=0)
table.plot(style={'M' : 'k-', 'F' : 'k--'})