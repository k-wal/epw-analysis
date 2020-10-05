import os

def write_year_counts(year, dir_path, output_file):
	file = open(dir_path + '/' + year + '/all.txt','r')
	lines = file.readlines()
	file.close()
	total = len(lines)

	try:
		file = open(dir_path + '/' + year + '/in_title.txt','r')
		lines = file.readlines()
		file.close()
		in_title = len(lines)
	except:
		in_title = 0

	try:
		file = open(dir_path + '/' + year + '/in_abstract.txt','r')
		lines = file.readlines()
		file.close()
		in_abstract = len(lines)
	except:
		in_abstract = 0

	to_write = [year, str(total), str(in_title), str(in_abstract)]
	to_write = '| ' + ' | '.join(to_write) + ' |\n'
	output_file.write(to_write)
	return


output_file = open('../dataset/counts.txt','w')
dir_path = '../dataset/final'
years = os.listdir('../dataset/final')
years.sort()

for year in years:
	write_year_counts(year, dir_path, output_file)
output_file.close()
