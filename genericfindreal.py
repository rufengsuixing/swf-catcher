import os, re, requests

res=''
#the download target folder
tar=''
#idm
with_idm=False
idmpath='C:/Program Files/app/IDM/IDMan.exe'

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Cache-Control': 'max-age=0'}

def idm_add_list(url,name,targetdir=tar,idmpath=idmpath):
    '''
    add the url into idm download list
    
    :Parameters:
        url : str
            The url of the file
        name : str
            The name of the download file you want
        targetdir : str
            The folder you want to put the file
    
    :return:`None`
    '''
    a=subprocess.Popen('"'+idmpath+'" /n /a /d "'+url+'" /p '+targetdir+' /f '+name)
    a.wait()
    a.kill()

for file in os.listdir(res):
    with open(os.path.join(path,file),'rb') as op:
        fin=re.findall(b'http(.*?)\.swf',op.read())
        for b in fin:
            try:
                b.decode('ascii')
            except:
                continue
            full='http'+b.decode()+'.swf'
            downname=full.split('/')[-1]
            name=downname.replace('-swf','').replace('.swf','')+'.swf'
            if os.path.isfile(tar+name):
                print(name,'exist')
                continue
            if with_idm:
                idm_add_list(full,name)
            else:
                st=requests.get(full,headers)
                if st.status_code==200:
                    with open(tar+name, "wb") as code:
                        code.write(st.content)
                    print(name,'downloaded')
                else:
                    print(name,'failed',st.status_code)