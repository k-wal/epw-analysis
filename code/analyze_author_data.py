import re
import sys
import os


# return array of categories, where argument is line as in input file
def get_categories_from_line(line):
	parts = re.split('\t', line)
	categories = parts[-1].strip()
	categories = [c.lower() for c in re.split(',',categories)]
	return categories

# return dictionaru of the form 'category' : total count
def get_category_counts(lines):
	counts = {}
	for line in lines:
		categories = get_categories_from_line(line)
		for c in categories:
			if c not in counts.keys():
				counts[c] = 0
			counts[c] += 1
	return counts


def write_categories_md(categories, counts, outfile):
	to_write =  "| # occurences | category |\n"
	to_write += "| ------------ | -------- |\n"
	outfile.write(to_write)
	for c in categories:
		to_write = "| " + str(counts[c]) + " | " + c + " |\n"
		outfile.write(to_write)

def write_categories_csv(categories, counts, outfile):
	for c in categories:
		to_write = str(counts[c]) + "," + c + "\n"
		outfile.write(to_write)

def write_category_counts(infile_path, outfile_path_csv, outfile_path_md):
	infile = open(infile_path, 'r')
	lines = infile.readlines()
	infile.close()

	counts = get_category_counts(lines)
	sorted_categories = sorted(counts, key = counts.get)
	sorted_categories.reverse()

	outfile_md = open(outfile_path_md, 'w')
	write_categories_md(sorted_categories, counts, outfile_md)
	outfile_md.close()

	outfile_csv = open(outfile_path_csv, 'w')
	write_categories_csv(sorted_categories, counts, outfile_csv)
	outfile_csv.close()

infile_path = '../dataset/re_authors_discipline.tsv'
outfile_path_csv = '../dataset/category_counts.csv'
outfile_path_md = '../dataset/category_counts.md'
write_category_counts(infile_path, outfile_path_csv, outfile_path_md)