import requests
from bs4 import BeautifulSoup 
import os
import re
import time
import random

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

def write_intitle(title,issue,authors,year,section):
	authors = authors.strip()
	issue = issue.strip()
	title = title.strip()
	to_write = [issue,section,title,authors]
	f = open(year + '/in_title.txt','a')
	f.write('||'.join(to_write) + '\n')
	f.close()

def write_inabstract(title,issue,authors,abstract,year,section):
	authors = authors.strip()
	issue = issue.strip()
	title = title.strip()
	abstract = abstract.strip()
	to_write = [issue,section,title,abstract,authors]
	f = open(year + '/in_abstract.txt','a')
	f.write('||'.join(to_write) + '\n')
	f.close()

def write_title(title,issue,authors,year,section):
	authors = authors.strip()
	issue = issue.strip()
	title = title.strip()
	to_write = [issue,section,title,authors]
	f = open(year + '/all_title.txt','a')
	f.write('||'.join(to_write) + '\n')
	f.close()

def write_abstract(title,issue,authors,abstract,year,section):
	authors = authors.strip()
	issue = issue.strip()
	title = title.strip()
	abstract = abstract.strip()
	to_write = [issue,section,title,abstract,authors]
	f = open(year + '/all_abstract.txt','a')
	f.write('||'.join(to_write) + '\n')
	f.close()


def write_issue(url,year):
	url = url.strip()
	issue = re.split('/',url)[-1]
	f = open(year + '/issues_done.txt','a')
	print(issue)
	f.write(issue +'\n')
	f.close()

def check_issue_done(url,year):
	if not os.path.isfile(year + '/issues_done.txt'):
		return False

	url = url.strip()
	issue = re.split('/',url)[-1] + '\n'
	f = open(year + '/issues_done.txt','r')
	lines = f.readlines()
	if issue in lines:
		return True
	return False
	f.close()




def get_text_jstor(url,year,section):
		headers = {'User-Agent' : 'Mozilla/5.0'}
		# headers = {'User-Agent' : 'Chrome/83.0.4103.116'}
		r = requests.get(url,headers=headers)
		soup = BeautifulSoup(r.content, 'lxml')
		title = soup.find('pharos-heading',class_='title-font') 		#title tag
		
		if not title:
			return

		if title.text.strip() == 'Front Matter':
			return
		
		print(title.text.strip())
		divs = soup.findAll('div',class_='turn-away-content__article-summary-journal')
		for div in divs:
			if div.find('a'):
				issue = div.find('a')

		authors = soup.find('div',class_='author-font')		#authors tag		

		if authors:
			write_title(title.text, issue.text, authors.text, year, section)
		else:
			write_title(title.text, issue.text, '', year, section)

		if check_presence(title.text):
			if authors:
				write_intitle(title.text, issue.text, authors.text, year, section)
			else:
				write_intitle(title.text, issue.text, '', year, section)


		heading = soup.find('pharos-heading',class_ = 'summary-header')

		if heading.text == 'Abstract':
			abstract = soup.find('p',class_='summary-paragraph')

			if authors:
				write_abstract(title.text, issue.text, abstract.text, authors.text, year, section)
			else:
				write_abstract(title.text, issue.text, abstract.text , '', year, section)

			if check_presence(abstract.text):
				if authors:
					write_inabstract(title.text, issue.text, abstract.text, authors.text, year, section)
				else:
					write_inabstract(title.text, issue.text, abstract.text , '', year, section)

		

def get_issue_urls(url,year):
	headers = {'User-Agent' : 'Mozilla/5.0'}
	# headers = {'User-Agent' : 'Chrome/83.0.4103.116'}
	r = requests.get(url,headers=headers)
	soup = BeautifulSoup(r.content, 'lxml')
	# print(soup.prettify)
	
	lis = soup.findAll('li', class_='row')
	url_divs = []

	total_divs = 0
	section_names = []

	for li in lis:
		if li.find('ul',class_ = 'no-bullet plxl'):
			break
		div = li.find('div',{'data-qa' : 'stable-url'})
		url_divs.append(div)
		section_names.append('----')

	for li in lis:
		if not li.find('ul', class_='no-bullet plxl'):
			continue
		divs = li.findAll('div', {'data-qa' : 'stable-url'})
		total_divs += len(divs)
		section = li.find('h3',class_="mln")
		#print(li)
		text = section.text.lower().strip()
		
		if 'letter' in text or 'editorial' in text:
			continue

		if 'review' in text and 'review of' not in text:
			continue

		url_divs.extend(divs)
		section_names.extend([text] * len(divs))
	
	for div,section in zip(url_divs,section_names):

		time.sleep(random.randint(5,10))
		get_text_jstor(div.text.strip(), year, section)

	write_issue(url, year)


def get_year_issues(url,year):
	year = str(year)
	if not os.path.isdir(year):
		os.mkdir(year)
	
	headers = {'User-Agent' : 'Mozilla/5.0'}
	r = requests.get(url,headers=headers)
	soup = BeautifulSoup(r.content, 'lxml')

	li = soup.find('li',{'data-year' : year})
	if not li:
		return

	links = li.findAll('a')
	for link in links:
		if check_issue_done('https://www.jstor.org'+link['href'], year):
			continue
		time.sleep(random.randint(3,5))
		get_issue_urls('https://www.jstor.org'+link['href'],year)


url = 'https://www.jstor.org/journal/econpoliweek?decade=2000'
get_year_issues(url, 2004)

# url = 'https://www.jstor.org/stable/i40033610'
# get_issue_urls(url,str(2010))

