import requests
import re
import os
import subprocess
#the html url eg:http://www.baidu.com
url=''
#the download target folder
tar=''
#idm
with_idm=False
idmpath='C:/Program Files/app/IDM/IDMan.exe'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Cache-Control': 'max-age=0'}
www='/'.join(url.split('/')[:3])
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
def findmain(strr):
    '''
    find the main content link address from the text of the html

    :Parameters:
        strr : str
            text of the html
    
    :rtype: str,[str,..]
    :return: a str show the common link is like
             a list show the link it found
    '''
    li=re.findall('href="(.*?)"',strr)
    def getsamepart(str1,str2):
        stli1=str1.split('/')
        stli2=str2.split('/')
        long=len(stli2)
        if len(stli1)<long:
            long=len(stli1)
        for a in range(0,long-1):
            if stli1[a]!=stli2[a]:
                return '/'.join(stli1[:a])
    def getsamecount(same):
        notsame=set(same)
        samedict={}
        for b in notsame:
            if b!=None and b!='':
                samedict[same.count(b)]=b
        return samedict
    li=[line.replace(www,'') for line in li]
    li=[a for a in li if len(a)>2]
    li.sort()
    same=[]
    for lineindex in range(0,len(li)-1):
        same+=[getsamepart(li[lineindex],li[lineindex+1])]
    samedict=getsamecount(same)
    mainhtml=samedict[[samedict.keys()].sort()[0]]
    return mainhtml,[line for line in li if line.find(mainhtml)!=-1]
def findpagelink(strr):
    '''
    find the page link address from the text of the html

    :Parameters:
        strr : str
            text of the html
    
    :rtype: [str,..]
    :return: a list show the pagelink it found
    '''
    li=re.findall('href="(.*?)".*?>\s*?(\d*?)\s*?<',strr)
    pages={}
    for link,page in li:
        pages[page]=link.replace(www,'')
    return pages
def getmainlink(mainhtml,strr):
    '''
    find the main content link address from the text of the html

    :Parameters:
        mainhtml: str
            the command part of the main link
        strr : str
            text of the html
    
    :rtype: [str,..]
    :return: a list show the mainlink it found
    '''
    li=re.findall('href="'+www+mainhtml+'(.*?)"',strr)
    return li
def downflash_r(link,with_idm=with_idm):
    '''
    find and download swf from the link

    :Parameters:
        link : str
            url of the html
        with_idm : bool
            if true add link into idm
    :return:`None`
    :stdout: if with_idm==False
                success print(name,'downloaded')
                failed print(name,'failed',status_code)
    '''
    st=requests.get(www+link,headers)
    source=re.findall('<param name=".*?" value="(.*?).swf',st.text)
    source=set(source)
    for b in source:
        b+='.swf'
        gamename=b.split('/')[-1].split('?')[0].replace('-swf','').replace('.swf','')+'.swf'
        if os.path.isfile(tar+name):
            print(name,'exist')
            continue
        if with_idm:
            idm_add_list(b,name)
        else:
            st=requests.get(b,headers)
            if st.status_code==200:
                with open(tar+name, "wb") as code:
                    code.write(st.content)
                print(name,'downloaded')
            else:
                print(name,'failed',st.status_code)
cachelink=[]
cachemain=[]
st=requests.get(url,headers=headers)
mainhtml,mainlink_r=findmain(st.text)
map(downflash_r,mainlink_r)
cachemain+=[a.replace(mainhtml,'') for a in mainlink_r]
while 1:
    pagelink_r=findpagelink(st.text)
    if pagelink_r==[]:
        print('sorry no new page found')
        exit()
    for onepage in pagelink_r :
        if onepage not in cachepage:
            cachepage+=onepage
            st=requests.get(www+onepage,headers=headers)
            mainlink_rr=getmainlink(mainhtml,st.text)
            for link_rr in mainlink_rr :
                if link_rr not in cachemain:
                    cachemain+=link_rr
                    downflash_r(mainhtml+link_rr)