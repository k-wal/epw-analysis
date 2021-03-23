import re
import os
import sys
from scrapers import academia_scraper

# function to scrape author data from academia and write to new file 
def write_academia_data(cur_filepath, new_filepath):
	infile = open(cur_filepath, 'r')
	lines = infile.readlines()
	infile.close()

	outfile = open(new_filepath, 'w')

	line = lines[1]
	# print(lines[0].split('\t'))
	# print(line.split('\t'))
	# print(lines[3].split('\t'))

	total = len(lines)
	for line in lines[1:] :
		parts = line.split('\t')
		n_articles = parts[0].strip()
		years_active = parts[1].strip()
		name = parts[2].strip()
		academia_url = parts[4].strip()
		other_url = parts[5].strip()
		discipline = parts[6].strip().lower()
		discipline = re.sub(', ', ',', discipline)

		# if discipline is not already present and academia url exists
		if discipline == '' and academia_url:
			discipline = academia_scraper.get_profile_disciplines(academia_url).lower()
		
		discipline = discipline.split(',')
		if len(discipline) > 3:
			discipline = discipline[0:3]
		discipline = ','.join(discipline)

		to_write = '\t'.join([n_articles, years_active, name, discipline])
		outfile.write(to_write + '\n')
		
		if total % 100 == 0:
			outfile.close()
			outfile = open(new_filepath, 'a')
		print(total)
		total -= 1
		
	outfile.close()


cur_filepath = '../dataset/authors_discipline.tsv'
new_filepath = '../dataset/re_authors_discipline.tsv'

write_academia_data(cur_filepath, new_filepath)