import os
import re
import matplotlib.pyplot as plt


abstract_counts1 = []
title_counts1 = []

abstract_counts2 = []
title_counts2 = []

def check_presence(text, keywords):
	if keywords == []:
		return True
	text = text.lower()
	for word in keywords:
		if word in text:
			return True
	return False


def get_year_counts(year, dir_path, keywords, abstract_counts, title_counts):
	file = open(dir_path + '/' + year + '/in_abstract.txt', 'r')
	lines = file.readlines()
	file.close()

	total_abstract = 0
	for line in lines:
		parts = re.split('\|\|', line.strip())
		abstract = parts[4]
		section = parts[1]
		if check_presence(abstract, keywords):
			total_abstract += 1
	abstract_counts.append(total_abstract)

	file = open(dir_path + '/' + year + '/in_title.txt', 'r')
	lines = file.readlines()
	file.close()

	total_title = 0
	for line in lines:
		parts = re.split('\|\|', line.strip())
		title = parts[3]
		if check_presence(title, keywords):
			total_title += 1
	title_counts.append(total_title)
	return abstract_counts, title_counts

# related to agriculture
# keywords1 = ['agriculture', 'agricultural', 'agrarian', 'crops', 'irrigat', 'farm', 'cropping']

# related to polution
# keywords1 = ['pollution','pollute','pollutant','contamination','smog','carbon','chemical','toxic','toxin','greenhouse','carbon','fossil fuel','emission','contaminant']

# related to resource management
# keywords1 = ['conservation', 'natural resources', 'fossil fuel', 'scarcity', 'crisis', 'renewable', 'sustainable']

#related to forest
# keywords2 = ['forest', 'wildlife', 'biodiversity', 'biosphere']
keywords1 = ['forest']
keywords2 = ['water']


dir_path = '../dataset/final'
years = os.listdir('../dataset/final')
draw = 0

years.sort()
years = years[:-1]

for year in years:
	abstract_counts1, title_counts1 = get_year_counts(year, dir_path, keywords1, abstract_counts1, title_counts1)
	abstract_counts2, title_counts2 = get_year_counts(year, dir_path, keywords2, abstract_counts2, title_counts2)


plt.plot(list(range(int(years[0]), int(years[-1])+1)), abstract_counts1, 'r', label= ','.join(keywords1))
plt.plot(list(range(int(years[0]), int(years[-1])+1)), abstract_counts2, 'b', label= ','.join(keywords2))
plt.title('keywords : ' + ','.join(keywords1) + '-' + ','.join(keywords2))
plt.ylabel('number of articles')
plt.xlabel('year')
plt.legend()
print('-'.join(keywords1) + '&&' + '-'.join(keywords2) + '.png')

if draw:
	if keywords1 == [] and keywords2 == []:
		plt.savefig('../graphs/all.png', bbox_inches='tight')
	else:
		plt.savefig('../graphs/' + '-'.join(keywords1) + '&&' + '-'.join(keywords2) + '.png', bbox_inches='tight')
		print('-'.join(keywords1) + '&&' + '-'.join(keywords2) + '.png')

plt.show()
