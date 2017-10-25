"# botstudy" 

def pick17sing():
    for i in range(10):
        # "%08d" %n = 強制抓8個字元, 當N不滿8位數時補0
        # "random.randint(0,1e8)  1e8 10的8次方
        songid  = "%08d" % random.randint(0,1e8)
        prefixlink  = 'http://17sing.tw/share_song/index.html?sid='
        link = prefixlink + songid
        
        oplink = urllib.request.urlopen(link)
        soup = BeautifulSoup(oplink, 'html.parser')
        songinfo = soup.find("meta",{"property":"og:description"})
        songcontext = songinfo.attrs["content"]
        if len(songcontext) > 0 :
            return link
        else:
            pass
    return "Try again!"
    
    
    2 http://www.cwb.gov.tw/V7/prevent/typhoon/Data/PTA_NEW/index.htm?dumm=Wed
    
