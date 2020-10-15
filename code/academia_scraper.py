import requests
from bs4 import BeautifulSoup 
import os
import re
import json

def get_profile_disciplines(url):
	headers = {'User-Agent' : 'Mozilla/5.0'}
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	scripts = []


	for s in soup.findAll('script'):
		try:
			t = s.keys()
		except:
			scripts.append(s)
		
	# print(scripts)

	interests = []
	for s in scripts:
		script = str(s)
		script = re.sub('<script>','',script)
		script = re.sub('</script>','',script)
		# print(script)
		if 'first_name' not in script or 'viewedUser' not in script or 'page_name' not in script:
			continue
		script = script.split('\n')[0][35:-2]
		data = json.loads(script)
		for interest in data['interests']:
			interests.append(interest['name'])
		print(interests)


url = 'https://iiit.academia.edu/RadhikaKrishnan'
url = 'https://independent.academia.edu/ShaliniBhutani'
url = 'https://iiit.academia.edu/AlokDebnath'
get_profile_disciplines(url)