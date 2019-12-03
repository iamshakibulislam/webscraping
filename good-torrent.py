from bs4 import BeautifulSoup
import requests
from xlsxwriter import Workbook

opp=requests.get('http://good-torrent.com')
soup=BeautifulSoup(opp.content,'lxml')
all_contents=soup.find('div',class_='hpC')
names_of_headers=[]
for x in all_contents.find_all('h2'):
	names_of_headers.append(x.a.string)
subhead=[]
latest=all_contents.find_all('h3',class_='cgray')
for x in latest:
	subhead.append(x.string)





lates_everything=[x for x in subhead if subhead.index(x)%2==0]


populer_everything=[x for x in subhead if subhead.index(x)%2!=0]



x=all_contents.find_all('div',class_='infScroll-inner')

l=x[0].find_all('li')
latestmovies=[c.a.span.string for c in l]

populer_movies=[c.a.span.string for c in x[1].find_all('li')]



latest_tv_shows=[c.a.span.string for c in x[2].find_all('li')]

populer_tv_shows=[c.a.span.string for c in x[3].find_all('li')]

latest_games=[c.a.span.string for c in x[4].find_all('li')]

populer_games=[c.a.span.string for c in x[5].find_all('li')]

latest_music=[c.a.span.string for c in x[6].find_all('li')]

populer_music=[c.a.span.string for c in x[7].find_all('li')]
import os
import xlsxwriter
if os.path.exists('good-torrent.xlsx'):
	os.remove('good-torrent.xlsx')
workbook=xlsxwriter.Workbook('good-torrent.xlsx')
sheet=workbook.add_worksheet()
for x in lates_everything:
	sheet.write(0,lates_everything.index(x),x)
for x in latestmovies:
	sheet.write(latestmovies.index(x)+1,0,x)
	
for x in latest_tv_shows:
	sheet.write(latest_tv_shows.index(x)+1,1,x)

for x in latest_games:
	sheet.write(latest_games.index(x)+1,2,x)
for x in latest_music:
	sheet.write(latest_music.index(x)+1,3,x)


for x in populer_everything:
	sheet.write(14,populer_everything.index(x),x)


for x in populer_movies:
	sheet.write(populer_movies.index(x)+16,0,x)
	
for x in populer_tv_shows:
	sheet.write(populer_tv_shows.index(x)+16,1,x)

for x in populer_games:
	sheet.write(populer_games.index(x)+16,2,x)
for x in populer_music:
	sheet.write(populer_music.index(x)+16,3,x)



workbook.close()




