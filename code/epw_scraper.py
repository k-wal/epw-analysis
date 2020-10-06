import requests
from bs4 import BeautifulSoup 
import os
import re


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


def get_article_text(url, output_path):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")

	# getting subject
	try:
		subject = soup.findAll('div', class_='field field-name-field-category field-type-taxonomy-term-reference field-label-hidden')[-1].text
		subject = subject.lower()
	except:
		subject = '-------'

	# dont print if editorial or letter in the subject, or if it is a book review
	if 'editorial' in subject or 'letter' in subject:
		return

	if 'review' in subject and 'review of' not in subject:
		return

	# getting title
	title = soup.find('title').text
	title = re.split('\|',title)[0].strip()

	# getting date and year
	time = soup.find('meta', {'property' : 'article:published_time'})['content']
	reverse_date = re.split('T',time)[0]
	split_date = re.split('-',reverse_date)
	split_date.reverse()
	year = split_date[-1]

	date = '-'.join(split_date)

	# getting abstract
	try:
		abstract = soup.find('meta', {'itemprop' : 'description'})['content']
	except:
		abstract = '------------------'

	# getting authors
	authors = []
	try:
		author_div = soup.find('div',{'class' : 'textformatter-list'})
		links = author_div.findAll('a')
		for link in links:
			authors.append(link.text)
	except:
		pass


	article_number = '---------'

	if not os.path.isdir(output_path + '/' + year):
		os.mkdir(output_path + '/' + year)

	# writing in files
	write_with_abstract(title, date, article_number, authors, abstract, year, subject, output_path+'/'+year+'/all.txt')
	if check_presence(title):
		write_without_abstract(title, date, article_number, authors, year, subject, output_path+'/'+year+'/in_title.txt')
	if check_presence(abstract):
		write_with_abstract(title, date, article_number, authors, abstract, year, subject, output_path+'/'+year+'/in_abstract.txt')

	print(title)



def get_issue_articles(url, output_path):
	print(url)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'lxml')
	divs = soup.findAll('div', class_='views-field views-field-title')

	for div in divs:
		if div.find('span'):
			continue
		link = div.find('a')['href']
		link = 'https://www.epw.in' + link
		get_article_text(link, output_path)
	print('\n\n')



def get_year_articles(url, year, output_path):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'lxml')
	tags = soup.findAll('fieldset', class_='collapsible collapsed')

	for tag in tags:
		if str(year) == tag.find('span').text:
			links = tag.findAll('a')
			for link in links:
				url = 'https://www.epw.in' + link['href']
				get_issue_articles(url, output_path)

url = 'https://www.epw.in/journal/epw-archive'
get_year_articles(url, 2015, '../dataset/final')