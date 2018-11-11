# -*- coding: utf-8 -*-  #
import os
import urllib.parse
import urllib.request
import gzip
import json
import random
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

os.system('help\kaishi.exe')
os.system('cls')
i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("Apagando las luces")(window.close)')
os.system('cls')
dict1 = dict(
             你好='How are you,what can i help you',\
             你叫什么名字='My name is jarvis',\
             你主人的信息='My master x.h. 16 is henan university freshmen，He is a ghost\
                           livestock industry a new star，Descendants of henan university of tai chi chuan，\
                           He determined to stand in the height of the programming community in the future\
                           Maybe this is life',\
             你的名字='My name is jarvis',\
             你有什么兴趣爱好吗='沉迷鬼畜，不可自拔',\
             你的爱好是什么='沉迷鬼畜，不可自拔',\
             来聊聊天吧='我们不是一直在聊天吗',\
             你有什么功能='陪我的主人聊天',\
             
             你的主人='My master is dong yuan terminator x.h.',\
             你的主人是谁='My master is dong yuan terminator x.h.',\
             你的生日是什么时候='我初次诞生是在贰零一七年四月二十五日的下午，天空一声巨响，贾维斯闪亮登场',\
             有道翻译='Translation model',\
             唱首歌吧='这个问题...因为主人的五音不全,所以我被取消了唱歌功能,玩些其他的吧，比如一起学习英语啊',\
             谢谢='不用谢，对我来说是小菜一碟的事。',\
             谢了='你太客气了，跟我还客气什么啊！',\
             唱歌='我会唱好多歌？想听吗？',\
             算了='那该怎么办？',\
             新闻='新华社报道:昨日晚间,天津市有个包子去打狗,就再也没有回来……',\
             什么='不知道',\
             天气='请输入您的所在地',\
             查询天气='请输入您的所在地',\
             天气天气='请输入您的所在地',\
             贾维斯='I am in',\
             胡的正='到！',\
             翻译='Translation model',\
             来首音乐='正在随机选择音乐',\
             视频='正在查找',\
             音乐='正在查找',\
             ip查看='正在检查本机IP',\
             IP='正在检查本机IP',\
             ip='正在检查本机IP',\
             信息发送='正在查找服务端',\
             信息接收='5150端口开启，正在等待数据输入',\
             打开学习助手='教程辅助正在打开',\
	     病毒释放='暂不提供，请手动释放',\
             联系计院服务器='正在启动程序...',\
             计院服务器='正在启动程序...',\
             联系服务器='正在启动程序...',\
             跳舞='额，请稍等...',\
             说我爱你='爸爸，我爱你',\
             打开编程指南='正在打开',\
             ) 
while  1 :
    a = input()
    if a =='有道翻译' or a == '翻译':
        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % dict1[a])
        while 1 :
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
            data = {}
            data['type'] = 'AUTO' 
            data['i'] = input('请输入要翻译的内容：')
            if data['i']=='break':                
                break;
            data['doctype'] = 'json'
            data['xmlVersion'] = '1.8'
            data['keyfrom']= 'fanyi.web'
            data['ue'] = 'UTF-8'
            data['typoResult'] = 'true'
            data = urllib.parse.urlencode(data).encode('utf-8')
            x = urllib.request.urlopen(url,data)
            h = x.read().decode('utf-8')
            t = json.loads(h)
            fy = t['translateResult'][0][0]['tgt']
            print(fy)
            i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % fy)
    if a!='有道翻译'and a!='翻译' and a!='天气' and a!='查询天气' and a!='关机' and a!='添加注销计划' and a!='打开编程助手' and a!='取消注销计划' and a!='计院服务器' and a!='联系服务器' and a!='跳舞':
        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % dict1[a])
        if a=='联系计院服务器' :
            os.system('help\fwqlx.exe')
        if a=='信息接收' :
            os.system('help\FWD.exe')
        if a=='信息发送' :
            os.system('help\KHD.exe')
        if a=='ip查看' or a=='ip' or a=='IP':
            os.system('help\ip.exe')
        if a=='打开学习助手':
            os.system('help\huye.chm')
        if a=='来首音乐' or a=='音乐':
            m = random.randint(0,21)
            os.system('music\%s.mp3' % m)
        if a=='视频':
            n = random.randint(0,43)
            os.system('voide\%s.mp4' % n)
    if a=='打开编程指南' :
        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % dict1[a])
        os.system('help\编程指南')
    if a=='跳舞':
        os.system('f\\0.mp3')
        os.system('f\\dong2.exe')
    if a=='计院服务器' or a=='联系服务器' :
        os.system('help\\fwqlx.exe')
    if a=='取消注销计划':
        os.system('shutdown -a')
    if a=='关机' or a=='添加注销计划':
        os.system('shutdown -s -t 60')
        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("计划添加成功，关机倒计时60秒")(window.close)')
    if a=='天气' or a=='查询天气':
            i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % dict1[a])
            while 1 :
                xx = 100
                if xx==101:
                    break
                
                def get_weather_data() :
                    city_name = input('请输入要查询的城市名称：')
                    if city_name=='break':
                        xx =101 
                    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
                    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
                    weather_data = urllib.request.urlopen(url1).read()
                    weather_data = gzip.decompress(weather_data).decode('utf-8')
                    weather_dict = json.loads(weather_data)
                    return weather_dict
                
                def show_weather(weather_data):
                
                    weather_dict = weather_data 
                    #将json数据转换为dict数据
                    if weather_dict.get('desc') == 'invilad-citykey':
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("你输入的城市名有误，退出天气查询")(window.close)')
                    elif weather_dict.get('desc') =='OK':
                        forecast = weather_dict.get('data').get('forecast')
                        print('城市：',weather_dict.get('data').get('city'))
                        print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
                        print('感冒：',weather_dict.get('data').get('ganmao'))
                        print('风向：',forecast[0].get('fengxiang'))
                        print('风级：',forecast[0].get('fengli'))
                        print('高温：',forecast[0].get('high'))
                        print('低温：',forecast[0].get('low'))
                        print('天气：',forecast[0].get('type'))
                        print('日期：',forecast[0].get('date'))
                        print('*******************************')
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("城市：%s")(window.close)' % weather_dict.get('data').get('city'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("温度：%s")(window.close)' % weather_dict.get('data').get('wendu'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("感冒：%s")(window.close)' % weather_dict.get('data').get('ganmao'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("风向：%s")(window.close)' % forecast[0].get('fengxiang'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("风级：%s")(window.close)' % forecast[0].get('fengli'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % forecast[0].get('high'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % forecast[0].get('low'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("天气：%s")(window.close)' % forecast[0].get('type'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("日期：%s")(window.close)' % forecast[0].get('date'))
                        i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("是否要显示未来四天天气，是,否")(window.close)')
                        four_day_forecast =input('是否要显示未来四天天气，是，或，否：')
                       
                        if four_day_forecast == '是' or four_day_forecast=='Y' or four_day_forecast=='y':
                            for i in range(1,5):
                                print('日期：',forecast[i].get('date'))
                                print('风向：',forecast[i].get('fengxiang'))
                                print('风级：',forecast[i].get('fengli'))
                                print('高温：',forecast[i].get('high'))
                                print('低温：',forecast[i].get('low'))
                                print('天气：',forecast[i].get('type'))
                                print('--------------------------')
                                i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("日期%s")(window.close)' % forecast[i].get('date'))
                                i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("风向%s")(window.close)' % forecast[i].get('fengxiang'))
                                i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("风级%s")(window.close)' % forecast[i].get('fengli'))
                                i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % forecast[i].get('high'))
                                i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % forecast[i].get('low'))
                                i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("天气%s")(window.close)' % forecast[i].get('type'))
                show_weather(get_weather_data())

    
