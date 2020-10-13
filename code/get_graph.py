import os
import re
import matplotlib.pyplot as plt


abstract_counts = []
title_counts = []

def check_presence(text, keywords):
	if keywords == []:
		return True
	text = text.lower()
	for word in keywords:
		if word in text:
			return True
	return False


def get_year_counts(year, dir_path, keywords):
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


dir_path = '../dataset/final'
years = os.listdir('../dataset/final')
keywords = []
draw = 0

years.sort()
years = years[:-1]

for year in years:
	get_year_counts(year, dir_path, keywords)

ratio = []
for a,t in zip(abstract_counts,title_counts):
	if t == 0:
		ratio.append(0)
	else:
		ratio.append(a/t)

plt.plot(list(range(int(years[0]), int(years[-1])+1)), abstract_counts, 'r', label='# abstract')
plt.plot(list(range(int(years[0]), int(years[-1])+1)), title_counts, 'b', label='# title')
# plt.plot(list(range(int(years[0]), int(years[-1])+1)), ratio, 'g', label='ratio')
plt.title('keywords : ' + ', '.join(keywords))
plt.ylabel('number of articles')
plt.xlabel('year')
plt.legend()

if draw:
	if keywords == []:
		plt.savefig('../graphs/all.png')
	else:
		plt.savefig('../graphs/' + '-'.join(keywords) + '.png')

plt.show()
