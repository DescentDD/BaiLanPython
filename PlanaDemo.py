import requests,json
from playsound import playsound
#key=sk-3f9d378c1d01e01351780bbc546c240fAPIGPT-v2
print('这是得得喵喵做的小爱,得得喵喵叫她Planetarium，也就是普拉娜！！！\n得得喵喵超级可爱！！\nKyrie eleison.\nChriste eleison.\nKyrie eleison.\n')
url='https://v.api.aa1.cn/api/api-xiaoai/talk.php'
res=requests.get(url)
if(res.status_code==200):
    print('吾等所盼乃七之哀叹\n吾等所忆耶利哥的古则\n得得喵喵OS的常驻管理员兼主系统P.L.A.N.A,待命中')
    while(1):
        text=input('你说：')
        Yoururl=f'https://v.api.aa1.cn/api/api-xiaoai/talk.php?msg={text}&type=json'
        chat=requests.get(Yoururl)
        jsoNMB=json.loads(chat.text)
        audioUrl=jsoNMB['meta']['music']['musicUrl']
        print('回答获取成功……')
        #print(audioUrl)
        audio=requests.get(audioUrl)
        print('音频捕获成功……')
        with open('audio.mp3','wb')as file:
            file.write(audio.content)
            print('写入成功……')
        print('P.L.A.N.A回答：━━━━━━───23:59:15 ⇆ ↻')
        playsound('audio.mp3')