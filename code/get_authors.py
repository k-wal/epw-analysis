import os
import re

# return all_authors with counts added for authors of 'year'
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

# write authors int file of 'outpath' in md table format
def write_all_authors(all_authors, outpath):
	outfile = open(outpath, 'w')
	all_authors = sorted(all_authors.items(), key=lambda x: x[1], reverse=True)
	outfile.write('| # articles | Author |\n')
	outfile.write('| ---------- | ------ |\n')

	for author in all_authors:
		if author[0] == '':
			continue
		to_write = '| ' + str(author[1]) + ' | ' + author[0] + ' |\n'
		outfile.write(to_write)
	outfile.close()


all_authors = {}
dir_path = '../dataset/final'
outpath = '../dataset/author_counts.md'
years = os.listdir('../dataset/final')
years.sort()
years = years[:-1]

# get authors for all years in all_authors
for year in years:
	all_authors = get_year_authors(year, dir_path, all_authors)

# write authors and counts in file
write_all_authors(all_authors, outpath)

