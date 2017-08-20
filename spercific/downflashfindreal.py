import os, re, requests
headers={'Host': 'sexflashgame.org',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0'}

path = 'C:\\Users\\yuan\\Desktop\\tmp\\'
tar=''
for file in os.listdir(path):
    with open(os.path.join(path,file),'rb') as op:
        fin=re.findall(b'http://sexflashgame\.org/wp-content/uploads/(.*?)\.swf'+b'\x00',op.read())
        for b in fin:
            downname=b.decode()+'.swf'
            name=downname.replace('-swf','').replace('.swf','')+'.swf'
            if os.path.isfile(tar+name):
                print(name,'exist')
                continue
            st=requests.get('http://sexflashgame.org/wp-content/uploads/'+downname,headers)
            if st.status_code==200:
                with open(tar+name, "wb") as code:
                    code.write(st.content)
                print(name,'downloaded')
            else:
                print(name,'failed',st.status_code)