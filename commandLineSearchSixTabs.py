import sys, webbrowser, bs4, requests

searchList = sys.argv[1:] # The search term needs to be entered in the command line

typedTerm = ''

for i in range(len(searchList)):
    typedTerm += searchList[i]
    typedTerm += ' '

searchPref = 'https://www.google.com/search?q='

searchTerm = searchPref+typedTerm

res = requests.get(searchTerm)
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

elems = noStarchSoup.select('div > a')

for i in elems[7:9]:
        webbrowser.open('https://www.google.com'+i["href"])





        
    
