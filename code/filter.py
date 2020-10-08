import os
import re

def check_presence(text):
	text = text.lower()
	keywords = ['environmental', 
	'ecology', 
	'ecological', 
	'environment-friendly', 
	'climate change', 
	'wildlife', 
	'forest', 
	'water', 
	'pollution',
	'conservation',
	'mineral extraction']

	for word in keywords:
		if word in text:
			return True

	if 'environment' in text:
		if 'nature' in text or 'natural' in text or 'earth' in text:
			return True

	if 'displacement' in text:
		for word in ['industry', 'industrial', 'mining', 'dams', 'dam', 'land']:
			if word in text:
				return True

	return False

def write_without_abstract(title,date,article_id,authors,year,section,output_path):
	to_write = [date,section,article_id,title,authors]
	f = open(output_path,'a')
	f.write('||'.join(to_write) + '\n')
	f.close()


def write_with_abstract(title,date,article_id,authors,abstract,year,section,output_path):
	to_write = [date,section,article_id,title,abstract,authors]
	f = open(output_path,'a')
	f.write('||'.join(to_write) + '\n')
	f.close()

def write_year_files(year, dir_path):
	file = open(dir_path + '/' + year + '/all.txt', 'r')
	lines = file.readlines()
	file.close()

	title_path = dir_path + '/' + year + '/in_title.txt'
	abstract_path = dir_path + '/' + year + '/in_abstract.txt'
	title_file = open(title_path, 'w')
	title_file.close()
	abstract_file = open(abstract_path, 'w')
	abstract_file.close()


	for line in lines:
		try:
			parts = re.split('\|\|', line.strip())
			date = parts[0]
			section = parts[1]
			article_id = parts[2]
			title = parts[3]
			abstract = parts[4]
			authors = parts[5]

			if check_presence(title):
				write_without_abstract(title,date,article_id,authors,year,section,title_path)
			if check_presence(abstract):
				write_with_abstract(title,date,article_id,authors,abstract,year,section,abstract_path)
		except:
			continue

dir_path = '../dataset/final'
years = os.listdir('../dataset/final')
years.sort()

for year in years:
	write_year_files(year, dir_path)
