import os
import re
import sys

# get (title, abstract) of articles of an author
def get_year_articles(year, dir_path, author_name):
	year_abstracts = []
	year_titles = []
	file = open(dir_path + '/' + year + '/in_abstract.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		parts = re.split('\|\|', line.strip())
		authors = parts[5]
		for author in re.split(',',authors):
			author = author.upper()
			author = re.sub('\.', '', author)
			if author == author_name:
				year_titles.append(parts[3])
				year_abstracts.append(parts[4])
				break

	return year_abstracts, year_titles

# main functions, takes author name and final corpus path
def main(author_name, dir_path):
	years = os.listdir(dir_path)
	years.sort()
	years = years[:-1]
	for year in years:
		abstracts , titles = get_year_articles(year, dir_path, author_name)
		if titles == []:
			continue
		print(year)
		print("\n")
		for t,a in zip(titles,abstracts):
			print("==== "+t+" =====")
			print(a)
			print("\n")
		print("-"*20)

dir_path = '../dataset/final'
main(sys.argv[1].upper(), dir_path)