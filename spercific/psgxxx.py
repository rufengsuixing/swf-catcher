import requests, re, os
tar=''
urls=['http://playsexgames.xxx/']
for a in range(2,25):
    urls.append('http://playsexgames.xxx/page/'+str(a)+'/')

headers={
   'Accept': 'text/html, */*; q=0.01',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-AU; q=0.5, en; q=0.3',
   'Connection': 'Keep-Alive',
   'Host': 'playsexgames.xxx',
   'Referer': 'http://playsexgames.xxx/',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
   'X-Requested-With': 'XMLHttpRequest'}
for url in urls:
    st=requests.get(url,headers=headers)
    target=re.findall('<a href="http://playsexgames\.xxx/.*?/"><img src="http://playsexgames\.xxx/play-sex-games/(.*?)\.jpg"',st.text)
    for a in target:
        name=a+'.swf'
        if os.path.isfile(tar+name):
            print(name,'exist')
            continue
        st=requests.get('http://playsexgames.xxx/play-sex-games/'+name,headers)
        if st.status_code==200:
                with open(tar+name, "wb") as code:
                    code.write(st.content)
                print(name,'downloaded')
        else:
            print(name,'failed',st.status_code)