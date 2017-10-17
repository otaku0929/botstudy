import requests
import random
from bs4 import BeautifulSoup

def yt():

    url = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/featured"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
   
    content = ""
    list = ""
       
    for count in range(1,6):      
        all_mv = soup.select("h3.yt-lockup-title a[dir='ltr']")
        for index, data in enumerate(all_mv):
            if index == random.randint(1,115):               
                break
            else:
                url="https://www.youtube.com{}".format(data.get("href"))
                title=format(data.get("title"))
                list = '{}\n{}\n\n'.format(title, url)
        content += list
        count += 1
    
    return(content)

def yt1():

    url = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/featured"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
   
    content = ""
      
    all_mv = soup.select("h3.yt-lockup-title a[dir='ltr']")
    for index, data in enumerate(all_mv):
        if index == random.randint(1,115):               
            url="https://www.youtube.com{}".format(data.get("href"))
            title=format(data.get("title"))
            list = '{}\n{}\n\n'.format(title, url)
    content += list
    
    return(content)

def yt2():

    url = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/featured"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
   
    content = ""
       
    for count in range(1,6):
        list=""
        all_mv = soup.select("h3.yt-lockup-title a[dir='ltr']")
        for index, data in enumerate(all_mv):
            if index == random.randint(1,110):
                return(list)
            url="https://www.youtube.com{}".format(data.get("href"))
            title=format(data.get("title"))
            list = '{}\n{}\n\n'.format(title, url)        
        count += 1
    content += list

def pt():
    content=yt2()
    #content=range()
    print(content)

if __name__ == '__main__':
    print(pt())
