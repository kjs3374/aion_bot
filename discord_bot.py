import discord
import requests
import json
import os
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
        
        
access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
