#proj2.py
import requests
from bs4 import BeautifulSoup
import ssl
import urllib.request, urllib.parse, urllib.error

### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for story_heading in soup.find_all(class_="story-heading", limit=10): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip()) 
	

### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

## Your Problem 2 solution goes here
base_url = 'http://www.michigandaily.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for div in soup.find_all(class_="panel-pane pane-mostread"):
	for link in div.find_all('a'):
		p=link.contents[0]
		print(p)



### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

## Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for img in soup.find_all('img'):
	if img.get('alt') == None:
		print('No alternative text provided!')
	else:
		print(img.get('alt'))


### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

## Your Problem 4 solution goes here
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


count=1
for i in range(6):
	url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page={}".format(i)

	r = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
	html = urllib.request.urlopen(r, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')


	contact_link=[]
	for content in soup.find_all(class_='field-item even'):
		for link in content.find_all('a'):
			if link.text == "Contact Details":
				contact_link.append(link.get('href')[1:])

	for each in contact_link:
		url='https://www.si.umich.edu/'+each
		r = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
		htmll = urllib.request.urlopen(r, context=ctx).read()
	
		soup1 = BeautifulSoup(htmll, 'html.parser')

		for content in soup1.find_all(class_='field-item even'):
			for link in content.find_all('a'):
				if "@" in link.text:
						print (str(count)+" "+link.text)
						count+=1


	