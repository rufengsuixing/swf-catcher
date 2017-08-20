'''

   请求 URL: http://www.gamesofdesire.com/files/img/blackhole-gloryhole-v1-1.jpg
   请求方法: GET
   状态码: 200 / OK
 - 请求标头
   Accept: image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5
   Accept-Encoding: gzip, deflate
   Accept-Language: zh-Hans-CN, zh-Hans; q=0.8, en-AU; q=0.5, en; q=0.3
   Cookie: source=3; _TotemToolUID=z42me-qjutt-rp30w
   Host: www.gamesofdesire.com
   Proxy-Connection: Keep-Alive
   Referer: http://www.gamesofdesire.com/action/girls-of-the-harem-frank-sophia/
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063



   Accept: 
   Accept-Encoding: gzip, deflate
   Accept-Language: zh-Hans-CN, zh-Hans; q=0.8, en-AU; q=0.5, en; q=0.3
   Host: www.gamesofdesire.com
   Proxy-Connection: Keep-Alive
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063
'''   
   
import requests, re, os

import subprocess
tar=''
def idm_add_list(url,name,targetdir=tar):
    a=subprocess.Popen('"C:/Program Files/app/IDM/IDMan.exe" /n /a /d "'+url+'" /p '+targetdir+' /f '+name)
    a.wait()
    a.kill()
headers={
   'Accept': '*/*',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-AU; q=0.5, en; q=0.3',
   'Connection': 'Keep-Alive',
   'Host': 'www.gamesofdesire.com',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
   }
for q in range(1,155):
    url='http://www.gamesofdesire.com/page/'+str(q)+'/'
    st=requests.get(url,headers=headers)
    target=re.findall('<a class="game_name" href="(.*?)">',st.text)
    print('page',q)
    for a in target:
        name=a.split('/')[2]+'.swf'
        if os.path.isfile(tar+name):
            print(name,'exist')
            continue
        st=requests.get('http://www.gamesofdesire.com/files/flash/'+name,headers,stream=True)
        if st.status_code==200 and int(st.headers['content-length'])>2000:
            idm_add_list('http://www.gamesofdesire.com/files/flash/'+name,name)
            print(name,'addtolist1')
            #with open(tar+name, "wb") as code:
            #    code.write(st.content)
            #print(name,'downloaded in page',q)
        else:
            #st=requests.get('http://www.gamesofdesire.com/3d/christie-s-room-the-transformation-final/',headers)
            st=requests.get('http://www.gamesofdesire.com'+a,headers)
            source=re.findall('<param name="movie" value="(.*?)"',st.text)
            if len(source)==0:
                with open(tar+name.replace('.swf','.html'), "wb") as code:
                    code.write(st.content)
                print(name.replace('.swf','.html'),'maybe html5 game')
                continue
            st=requests.get(source[0],headers,stream=True)
            if st.status_code==200:
                idm_add_list(source[0],name)
                print(name,'addtolist2')
                #with open(tar+name, "wb") as code:
                #    code.write(st.content)
                #print(name,'downloaded in page',q)
            else:
                print(name,'failed',st.status_code)