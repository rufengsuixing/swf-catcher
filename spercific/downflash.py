import requests
import re
import os
tar=''
urls=['http://sexflashgame.org/hentai-games/',
'http://sexflashgame.org/',
'http://sexflashgame.org/sex-games/',
'http://sexflashgame.org/adult-games/',
'http://sexflashgame.org/free-sex-games/',
'http://sexflashgame.org/free-porn-games/',
'http://sexflashgame.org/play-porn-games/',
'http://sexflashgame.org/play-sex-games/',
'http://sexflashgame.org/online-games/',
'http://sexflashgame.org/xxx-games/',
'http://sexflashgame.org/sexy-games/',
'http://sexflashgame.org/best-games-hentai/',
'http://sexflashgame.org/sex-flash-games/',
'http://sexflashgame.org/porn-flash-games/',
'http://sexflashgame.org/erotic-games/',
'http://sexflashgame.org/sex-cartoons/',
'http://sexflashgame.org/meet-and-fuck-games-demo/',
'http://sexflashgame.org/demo-porn-games/']
headers={'Host': 'sexflashgame.org',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0'}
for url in urls:
    st=requests.get(url,headers=headers)
    target=re.findall('<a href="(.*?)" rel=".*?">',st.text)
    #target=re.findall(r'http://sexflashgame\.org/wp-content/uploads/(.*?)\.jpg',st.text)
    for a in target:
        st=requests.get(a,headers)
        source=re.findall('<param name="base" value="(.*?)">',st.text)
        for b in source:
            name=b.split('/')[-1].split('?')[0].replace('-swf','').replace('.swf','')+'.swf'
            if os.path.isfile(tar+name):
                print(name,'exist')
                continue
            st=requests.get(b,headers)
            if st.status_code==200:
                with open(tar+name, "wb") as code:
                    code.write(st.content)
                print(name,'downloaded')
            else:
                print(name,'failed',st.status_code)