import os
import re

# return all_authors with counts added for authors of 'year'
def get_year_authors(year, dir_path, all_authors, author_years):
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
				author_years[author].append(year)
			else:
				all_authors[author] = 1
				author_years[author] = [year]
	return all_authors, author_years

# write authors int file of 'outpath' in md table format
def write_all_authors(all_authors, author_years, outpath):
	outfile = open(outpath, 'w')
	all_authors = sorted(all_authors.items(), key=lambda x: x[1], reverse=True)
	# outfile.write('| # articles | Years Active | Author | Academia URL | Alternate URL | \n')
	# outfile.write('| ---------- | ------------ | ------ | ------------ | ------------- |\n')
	outfile.write('# articles,Years Active,Author,Academia URL,Alternate URL\n')

	for author in all_authors:
		if author[0] == '':
			continue
		years_active = author_years[author[0]]
		year_span = min(years_active) + '-' + max(years_active)
		to_write = str(author[1]) + ',' + year_span + ',' + author[0] + '\n'
		# to_write = '| ' + str(author[1]) + ' | ' + year_span + ' | ' + author[0] + ' | | |\n'
		outfile.write(to_write)
	outfile.close()


all_authors = {}
author_years = {}
dir_path = '../dataset/final'
outpath = '../dataset/just_author_counts.csv'
years = os.listdir('../dataset/final')
years.sort()
years = years[:-1]

# get authors for all years in all_authors
for year in years:
	all_authors, author_years = get_year_authors(year, dir_path, all_authors, author_years)

# write authors and counts in file
write_all_authors(all_authors, author_years, outpath)

