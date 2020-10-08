import os
import re


def get_year_authors(year, dir_path, all_authors):
	file = open(dir_path + '/' + year + '/in_abstract.txt', 'r')
	lines = file.readlines()
	file.close()

	for line in lines:
		parts = re.split('\|\|', line.strip())
		authors = parts[5]
		for author in re.split(',',authors):
			author = author.upper()
			author = re.sub('\.', '', author)
			if author in all_authors.keys():
				all_authors[author] += 1
			else:
				all_authors[author] = 1
	return all_authors


def write_all_authors(all_authors, outpath):
	outfile = open(outpath, 'w')
	all_authors = sorted(all_authors.items(), key=lambda x: x[1], reverse=True)

	for author in all_authors:
		to_write = str(author[1]) + ' -- ' + author[0] + '\n'
		outfile.write(to_write)
	outfile.close()


all_authors = {}
dir_path = '../dataset/final'
outpath = '../dataset/author_counts.txt'
years = os.listdir('../dataset/final')
years.sort()
years = years[:-1]

for year in years:
	all_authors = get_year_authors(year, dir_path, all_authors)

write_all_authors(all_authors, outpath)

