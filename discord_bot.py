import discord
import requests
import json
from bs4 import BeautifulSoup


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("그래 나도 안녕")
    if message.content.startswith("잘가"):
        await message.channel.send("너도 잘가")
    if message.content.startswith("검색"):
        st, user = message.content.split()
        
        url = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user)
        req = requests.get(url).content

        data = json.loads(req)

        for item in data:
            charname = item['charname']
            if charname == user :
                uid = item['userid']

        aionurl = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        await message.channel.send (aionurl)
#    if message.content.startswith("검색"):
#        st, user = message.content.split()
        
#        url = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user)
#        req = requests.get(url).content

#        data = json.loads(req)

#        for item in data:
#            charname = item['charname']
#            if charname == user :
#                uid = item['userid']

#        aionurl = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
#        await message.channel.send (aionurl)
        
    if message.content.startswith("단체검색"):
        st, user1, user2, user3, user4, user5, user6 = message.content.split()
        
        url1 = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user1)
        url2 = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user2)
        url3 = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user3)
        url4 = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user4)
        url5 = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user5)
        url6 = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user6)
        
        req1 = requests.get(url1).content
        req2 = requests.get(url2).content
        req3 = requests.get(url3).content
        req4 = requests.get(url4).content
        req5 = requests.get(url5).content
        req6 = requests.get(url6).content

        data1 = json.loads(req1)
        data2 = json.loads(req2)
        data3 = json.loads(req3)
        data4 = json.loads(req4)
        data5 = json.loads(req5)
        data6 = json.loads(req6)

        for item in data1:
            charname = item['charname']
            if charname == user1 :
                uid = item['userid']

        aionurl1 = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        await message.channel.send (user1)
        await message.channel.send (aionurl1)
 
        for item in data2:
            charname = item['charname']
            if charname == user2 :
                uid = item['userid']

        aionurl2 = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        await message.channel.send (user2)
        await message.channel.send (aionurl2)        

        for item in data3:
            charname = item['charname']
            if charname == user3 :
                uid = item['userid']

        aionurl3 = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        await message.channel.send (user3)
        await message.channel.send (aionurl3)

        for item in data4:
            charname = item['charname']
            if charname == user4 :
                uid = item['userid']

        aionurl4 = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        await message.channel.send (user4)
        await message.channel.send (aionurl4)

        for item in data5:
            charname = item['charname']
            if charname == user5 :
                uid = item['userid']

        aionurl5 = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        await message.channel.send (user5)
        await message.channel.send (aionurl5)

        for item in data6:
            charname = item['charname']
            if charname == user6 :
                uid = item['userid']

        aionurl6 = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        await message.channel.send (user6)        
        await message.channel.send (aionurl6)        
        
        
    if message.content.startswith("!검색"):
        st, user = message.content.split()  
        
        url = 'http://reikop.com:8080/api/suggest?keyword={}&server=ISRAFEL'.format(user)
        req = requests.get(url).content

        data = json.loads(req)

        for item in data:
            charname = item['charname']            
            if charname == user :
                uid = item['userid']
                className = item['className']
                raceName = item['raceName']
                guildName = item['guildName']

        aionurl = 'https://aion.plaync.com/characters/server/21/id/{}/home'.format(uid)
        srcurl = 'http://reikop.com:8080/api/character/ISRAFEL/{}'.format(uid)

        reqsrc = requests.get(srcurl).content
        datasrc = json.loads(reqsrc)
        chrstat = datasrc['character_stats']
        #totstat = chrstat['totalStat']
        totstat = datasrc['character_stats']['totalStat']
        stigma = datasrc['character_stigma']
        equip = datasrc['character_equipments']
        
        stiName = []
        eqName = []
        for sti in stigma:
            stiName.append(sti['name'])
        for eq in equip:
            eqName.append(eq['name'])
        print(eqName)
        #변수매칭
        accuracy = totstat['accuracyRight']
        magicalAccuracy = totstat['magicalAccuracy']
        attack = totstat['physicalRight']
        hp = totstat['hp']
        magicResist = totstat['magicResist']
        critical = totstat['criticalRight']
        block = totstat['block']
        
        await message.channel.send\
        ("기본정보\n닉네임 : {} \n클래스 : {}\n종족 : {} \n레기온 : {}\
        \n\n스탯\n\n생명력 : {} \n마법저항 : {} \n방패방어 : {}\n공격력 : {} \n명중 : {} \n물리치명타 : {}\n마법적중 : {} \
        \n\n스티그마\n\n스티그마1 : {}\n스티그마2 : {}\n스티그마3 : {}\n스티그마4 : {}\n스티그마5 : {}\n스티그마6 : {}\n스티그마7 : {}\n스티그마8 : {}"
        .format(user,className,raceName,guildName,hp,magicResist,block,attack,accuracy,critical,magicalAccuracy,\
        stiName[0],stiName[1],stiName[2],stiName[3],stiName[4],stiName[5],stiName[6],stiName[7]))

        
        
        
client.run("ODM2ODU2Mjk2OTc1MTA2MDg4.YIkFKQ.XJ_-sjUEohHPzTQuxoUyPZu53IA")
