import urllib2 
import time
import android
import time as t
import sys
import ssl 
import glob
folder="/sdcard/extras/org.qpython.qpy/files/lib/python2.7/site-packages/*.egg"
for file in glob.glob(folder):
    sys.path.append(file)
from bs4 import BeautifulSoup
try: 
    _create_unverified_https_context = ssl._create_unverified_context 
except AttributeError: 
    pass
else: 
    ssl._create_default_https_context = _create_unverified_https_context 
droid = android.Android()
def parseResult(soup):
    res = ""
    divClass = [
        ('div','_XWk'),
        ('div','cwos'),
        ('div','curtgt'),
        ('div','kpd-ans'),
        ('div','vk_ans'),
        ('div','_sdf'),
        ('div','kltat'),
        ('div','_oDd'),
        ('div','_xHd'),
        #('div','Z0LcW'),
        ('div','gsrt'),
        #('div','vk_sh'),
        ('div','lr_dct_sf_sen'),
        ('div','sYYygf')
        
        
        
    
    ]
    for tag,className in divClass:
        
        if soup.findAll(tag,class_=className):
            if className == 'kltat':
                
                for q in soup.find_all(True,{"class":[className]}):
                    res += q.getText()+'\n'
                    print className
            elif className == 'sYYygf':
                
                for q in soup.find_all(True,{"class":[className]}):
                    res += q.getText()+'\n'
                    print className
            else:
                res += soup.find(tag,class_=className).getText()+"\n"
                print className
            
    
    if res:
        return res.encode("UTF-8")
    else:
        return "no result"
            
def getGoogleResult(query):
    print query
    query = query.replace(' ','+')
    url = "https://www.google.com/search?client=ms-android-blu&sourceid=chrome-mobile&ie=UTF-8&hl=en&q="+query+'&oq='+query
    opener = urllib2.build_opener() 
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 6.0.1; Life One X2 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Mobile Safari/537.36')] 
    #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        page = opener.open(url).read() 
        
    except:
        print 'no internet'
        return False
    
    soup = BeautifulSoup(page,'html.parser')
    s = parseResult(soup)
    print s
    return s
    #print soup.get_text().replace('&nbsp;','').encode('utf-8').strip()
    
    #html = opener.open(url).read() 
    #print s
    #print g.replace('&nbsp;','').encode('utf-8').strip()
    #print soup
    
    #print "-"*15+"Answer"+"-"*15
    
    #print s.replace('&nbsp;','').encode('utf-8').strip()
    #droid.ttsSpeak(s)
