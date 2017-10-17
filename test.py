import requests
import random
import re
from bs4 import BeautifulSoup


def ymovie():
    target_url = 'https://tw.movies.yahoo.com/movie_intheaters.html'
    request = requests.get(target_url)
    moviecontent = request.content
    soup = BeautifulSoup(moviecontent, 'html.parser')
    page_list = []
    #movie_list = []
    alist = []
    content = ""
    for page in range(1,6):
        page_url = 'http://tw.movies.yahoo.com/movie_intheaters.html?page={}'.format(page)
        page_list.append(page_url)

    while page_list:
        index = page_list.pop(0)
        res = requests.get(index)
        movie_list = ymovie_content(res)
        alist.append(movie_list)

    random.shuffle(alist)
    randommovie = alist[0:2]

   

    for data in randommovie:
        title = format(data.get("data-ga")[20:].strip("]"))
        url = format(data.get("href"))
        img = data.select('img')[0]['src']
        content += '{}\n{}\n{}\n\n'.format(title,url,img)

        
        #content += format(alist)
        
    

    #random.shuffle(list)
    #randomfivemv = list[0:3]
    
    return randommovie
    
def ymovie_content(res):
    #rescontent = res.content
    soup = BeautifulSoup(res.content,'html.parser')
    
    content = ""
    alist = soup.select("div.release_foto a[class='gabtn']")
    
  

    return alist

def y():
    target_url = 'https://tw.movies.yahoo.com/movie_intheaters.html'
    request = requests.get(target_url)
    moviecontent = request.content
    soup = BeautifulSoup(moviecontent, 'html.parser')

    movie_list = ""
    alist = soup.select("div.release_foto a[class='gabtn']")
    
    for list in soup.select("div.release_foto a[class='gabtn']"):
        a = list
        title = format(list.get("data-ga")[20:].strip("]"))
        url = format(list.get("href"))
        img = list.select('img')[0]['src']
        movie_list += '{}\n{}\n{}\n\n'.format(title,url,img) 

    return alist
    

def yt():

    url = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/featured?gl=TW#loc0=it"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
   
    content = ""
    ytlist= ""   

    all_mv = soup.select("h3.yt-lockup-title a[dir='ltr']")
    random.shuffle(all_mv)
    randomfivemv = all_mv[0:3]

    for data in randomfivemv:
        url="https://www.youtube.com{}".format(data.get("href"))
        title=format(data.get("title"))
        ytlist = '{}\n{}\n\n'.format(title, url)  
        content += ytlist
    return randomfivemv

def pt():

    content=ymovie()
    print(content)

def wt():
    content=yt()
    f=open('output.txt','w', encoding='UTF-8')
    f.write(format(content))
    f.close()
    print ('--print ok--')

if __name__ == '__main__':
    print(pt())
    #print(wt())


        #for data in list:
    #    title = format(list.get("data-ga")[20:].strip("]"))
    #    url = format(list.get("href"))
    #    img = list.select('img')[0]['src']
    #    content += '{}\n{}\n{}\n\n'.format(title,url,img)


