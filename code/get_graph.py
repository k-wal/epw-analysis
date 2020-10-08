import os
import re
import matplotlib.pyplot as plt


abstract_counts = []
title_counts = []

def check_presence(text):
	text = text.lower()
	keywords = ['forest']
	for word in keywords:
		if word in text:
			return True

	return False


def get_year_counts(year, dir_path):
	file = open(dir_path + '/' + year + '/in_abstract.txt', 'r')
	lines = file.readlines()
	file.close()

	total_abstract = 0
	for line in lines:
		parts = re.split('\|\|', line.strip())
		abstract = parts[4]
		if check_presence(abstract):
			total_abstract += 1
	abstract_counts.append(total_abstract)

	file = open(dir_path + '/' + year + '/in_title.txt', 'r')
	lines = file.readlines()
	file.close()

	total_title = 0
	for line in lines:
		parts = re.split('\|\|', line.strip())
		title = parts[3]
		if check_presence(title):
			total_title += 1
	title_counts.append(total_title)


dir_path = '../dataset/final'
years = os.listdir('../dataset/final')
years.sort()
years = years[:-1]

for year in years:
	get_year_counts(year, dir_path)

plt.plot(list(range(int(years[0]), int(years[-1])+1)), abstract_counts)
plt.plot(list(range(int(years[0]), int(years[-1])+1)), title_counts)
plt.show()