import requests                                         #importing requests library to send http request to the servers
from bs4 import BeautifulSoup                       #importing beautifulsoup for parsing the website
no_votes = int(input("enter the number of points you want : \n"))   #input from user for number of votes
for i in range(1,10):
    url = ("https://news.ycombinator.com/?p=" + str(i))
    link = requests.get(url)
    soup = BeautifulSoup(link.text, "lxml")
    hacker_news = soup.find_all("tr", class_ = "athing")
    try : 
        for i,new in enumerate(hacker_news):
                news = new.find("span", class_ = "titleline")
                a_tag = news.find("a")
                link = a_tag['href']
                scores = soup.select(".score")
                score = int(scores[i].text.split()[0])
                if (score >= no_votes ):
                    print(f"TITLE : {news.text}")
                    print(f"Link of news {i+1}: {link}")
                    print(f"Points of news {i+1} : {scores[i].text}")
                    print("\n")
                    
    except:
        print('')



