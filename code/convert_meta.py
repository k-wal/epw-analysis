from bs4 import BeautifulSoup as bs
import re
import os

def check_if_done(article_id,year,output_path):
	if not os.path.isdir(output_path + '/' + year):
		os.mkdir(output_path + '/' + year)
		file = open(output_path + '/' + year + '/done.txt','a')
		file.write(article_id + '\n')
		file.close()
		return False

	file = open(output_path + '/' + year + '/done.txt','r')
	lines = file.readlines()
	file.close()
	for line in lines:
		if article_id == line.strip():
			return True

	file = open(output_path + '/' + year + '/done.txt','a')
	file.write(article_id + '\n')
	file.close()
	return False

def check_presence(text):
	text = text.lower()
	keywords = ['environmental', 'ecology', 'ecological', 'environment-friendly']
	for word in keywords:
		if word in text:
			return True

	if 'environment' in text:
		if 'nature' in text or 'natural' in text or 'earth' in text:
			return True

	return False

def write_without_abstract(title,date,article_id,authors,year,section,output_path):
	authors = ",".join(authors)
	to_write = [date,section,article_id,title,authors]
	f = open(output_path,'a')
	f.write('||'.join(to_write) + '\n')
	f.close()


def write_with_abstract(title,date,article_id,authors,abstract,year,section,output_path):
	authors = ",".join(authors)
	to_write = [date,section,article_id,title,abstract,authors]
	f = open(output_path,'a')
	f.write('||'.join(to_write) + '\n')
	f.close()



def parse_single(path, output_path):
	f = open(path,'r')
	content = f.readlines()
	f.close()
	content = "".join(content)
	soup = bs(content,"lxml")

	# finding article number
	url = soup.find('self-uri')['xlink:href']
	article_number = re.split('/',url)[-1]

	# finding dates
	dates = soup.findAll('pub-date')
	beg = dates[0]
	year = beg.find('year').text.strip()
	beg_date = beg.find('day').text + '/' + beg.find('month').text + '/' + beg.find('year').text
	
	try :
		end = dates[1]
		end_date = end.find('day').text + '/' + end.find('month').text + '/' + end.find('year').text
	except:
		end_date = ' '
	
	# final date
	date = beg_date + '-'  + end_date

	if not os.path.isdir(output_path + '/' + year):
		os.mkdir(output_path + '/' + year)


	# checking to see if article has already been added
	# if check_if_done(article_number,year,output_path):
	# 	return

	# getting subject
	try:
		subject = soup.find('subject').text.lower().strip()
	except:
		subject = '------'

	# dont print if editorial or letter in the subject, or if it is a book review
	if 'editorial' in subject or 'letter' in subject:
		return

	if 'review' in subject and 'review of' not in subject:
		return

	# finding title
	title = soup.find('article-title').text.strip()
	if title in ["Front Matter", "Back Matter", "Statistics"]:
		return
	
	# finding authors
	authors = []
	for tag in soup.findAll('contrib'):
		try:
			fn = tag.find('given-names').text.strip()
			ln = tag.find('surname').text.strip()
			authors.append(fn + ' ' + ln)
		except:
			try:
				name = tag.find('string-name').text.strip()
				authors.append(name)
			except:
				continue

	# getting abstract
	try:
		abstract = soup.find('abstract').text.strip()
	except:
		abstract = "-------------------------------------"

	# writing in files
	write_with_abstract(title, date, article_number, authors, abstract, year, subject, output_path+'/'+year+'/all.txt')
	if check_presence(title):
		write_without_abstract(title, date, article_number, authors, year, subject, output_path+'/'+year+'/in_title.txt')
	if check_presence(abstract):
		write_with_abstract(title, date, article_number, authors, abstract, year, subject, output_path+'/'+year+'/in_abstract.txt')
		

def parse_all(path,output_path):
	i = 0
	for filename in os.listdir(path):
		parse_single(path+'/'+filename, output_path)
		print(i)
		i += 1
parse_all('../dataset/corpus','../dataset/final')
