import requests
import random
from bs4 import BeautifulSoup

def movie_new():

    alist = []
    for page in range(1,2):#collect movies from 5 page
        page_url = 'https://tw.movies.yahoo.com/movie_thisweek.html?page={}'.format(page)
        res = requests.get(page_url)
        movie_list = ymovie_content(res)
        for movie in movie_list:
            alist.append(movie)        
    
    #select 3 mobvies from 5 page
    random.shuffle(alist)
    randommovie = alist[0:5]

    #export movie information 
    content = ""
    for data in randommovie:
        title = format(data.get("data-ga")[23:].strip("]"))
        url = format(data.get("href"))
        #img = data.select('img')[0]['src']
        content += '本週上映{}\n{}\n\n'.format(title,url)

    return content
    
def ymovie_content(res):
    #rescontent = res.content
    soup = BeautifulSoup(res.content,'html.parser')
    
    content = ""
    alist = soup.select("div.release_foto a[class='gabtn']")
    
    return alist

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

def wt():
    content=ymovie()
    f=open('output.txt','w', encoding='UTF-8')
    f.write(format(content))
    f.close()
    print ('--print ok--')

if __name__ == '__main__':
    print(pt())
    #print(wt())
