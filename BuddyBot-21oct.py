#from sqlite3 import Time
import discord
from discord.ext import commands, tasks
#import asyncio
import time
#from time import sleep
import random
from discord import Member
import os
import asyncio
import googletrans
from io import BytesIO
#from typing import Union, Optional
from petpetgif import petpet as petpetgif
import requests
#import imagecomparison
import re
import flag
from datetime import datetime, timedelta
now = datetime.now()
#secondstillrun = ((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600))
#tdd = timedelta(seconds=secondstillrun)
futuretime = str((now + timedelta( seconds= ((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)) )).replace(microsecond=0))
#uturedate = now+tdd
#print(futuredate)
#timevalues = type('', (), {})()
#timevalues.value = [secondstillrun, futuredate]
#timevalues.stamp = futuredate
#def TimeMemRW(InputVV, read):
#    if read:
#        return timevalues.value
#    else:
#        timevalues.value = InputVV

def getNation(codein):
    langtonatexp = {
    'af': 'ZA',
    'agq': 'CM',
    'ak': 'GH',
    'am': 'ET',
    'ar': 'AE',
    'as': 'IN',
    'asa': 'TZ',
    'az': 'AZ',
    'bas': 'CM',
    'be': 'BY',
    'bem': 'ZM',
    'bez': 'IT',
    'bg': 'BG',
    'bm': 'ML',
    'bn': 'BD',
    'bo': 'CN',
    'br': 'FR',
    'brx': 'IN',
    'bs': 'BA',
    'ca': 'ES',
    'cgg': 'UG',
    'chr': 'US',
    'cs': 'CZ',
    'cy': 'GB',
    'da': 'DK',
    'dav': 'KE',
    'de': 'DE',
    'dje': 'NE',
    'dua': 'CM',
    'dyo': 'SN',
    'ebu': 'KE',
    'ee': 'GH',
    'en': 'GB',
    'el': 'GR',
    'es': 'ES',
    'et': 'EE',
    'eu': 'ES',
    'ewo': 'CM',
    'fa': 'IR',
    'fil': 'PH',
    'fr': 'FR',
    'ga': 'IE',
    'gl': 'ES',
    'gsw': 'CH',
    'gu': 'IN',
    'guz': 'KE',
    'gv': 'GB',
    'ha': 'NG',
    'haw': 'US',
    'he': 'IL',
    'hi': 'IN',
    'ff': 'CN',
    'fi': 'FI',
    'fo': 'FO',
    'hr': 'HR',
    'hu': 'HU',
    'hy': 'AM',
    'id': 'ID',
    'ig': 'NG',
    'ii': 'CN',
    'is': 'IS',
    'it': 'IT',
    'ja': 'JP',
    'jmc': 'TZ',
    'ka': 'GE',
    'kab': 'DZ',
    'ki': 'KE',
    'kam': 'KE',
    'mer': 'KE',
    'kde': 'TZ',
    'kea': 'CV',
    'khq': 'ML',
    'kk': 'KZ',
    'kl': 'GL',
    'kln': 'KE',
    'km': 'KH',
    'kn': 'IN',
    'ko': 'KR',
    'kok': 'IN',
    'ksb': 'TZ',
    'ksf': 'CM',
    'kw': 'GB',
    'lag': 'TZ',
    'lg': 'UG',
    'ln': 'CG',
    'lt': 'LT',
    'lu': 'CD',
    'lv': 'LV',
    'luo': 'KE',
    'luy': 'KE',
    'mas': 'TZ',
    'mfe': 'MU',
    'mg': 'MG',
    'mgh': 'MZ',
    'ml': 'IN',
    'mk': 'MK',
    'mr': 'IN',
    'ms': 'MY',
    'mt': 'MT',
    'mua': 'CM',
    'my': 'MM',
    'naq': 'NA',
    'nb': 'NO',
    'nd': 'ZW',
    'ne': 'NP',
    'nl': 'NL',
    'nmg': 'CM',
    'nn': 'NO',
    'nus': 'SD',
    'nyn': 'UG',
    'om': 'ET',
    'or': 'IN',
    'pa': 'PK',
    'pl': 'PL',
    'ps': 'AF',
    'pt': 'PT',
    'rm': 'CH',
    'rn': 'BI',
    'ro': 'RO',
    'ru': 'RU',
    'rw': 'RW',
    'rof': 'TZ',
    'rwk': 'TZ',
    'saq': 'KE',
    'sbp': 'TZ',
    'seh': 'MZ',
    'ses': 'ML',
    'sg': 'CF',
    'shi': 'MA',
    'si': 'LK',
    'sk': 'SK',
    'sl': 'SI',
    'sn': 'ZW',
    'so': 'SO',
    'sq': 'AL',
    'sr': 'RS',
    'sv': 'SE',
    'sw': 'TZ',
    'swc': 'CD',
    'ta': 'IN',
    'te': 'IN',
    'teo': 'UG',
    'th': 'TH',
    'ti': 'ER',
    'to': 'TO',
    'tr': 'TR',
    'twq': 'NE',
    'tzm': 'MA',
    'uk': 'UA',
    'ur': 'PK',
    'uz': 'UZ',
    'vai': 'LR',
    'vi': 'VN',
    'vun': 'TZ',
    'xog': 'UG',
    'yav': 'CM',
    'yo': 'NG',
    'zh': 'CN',
    'zu': 'ZA'
  }
    try:
        return langtonatexp[codein]
    except:
        return None


#import traceback
setprefix = "//"
petalias=["pat","petpet","patpat"]
petaliaspref = [setprefix + sub for sub in petalias]
petaliaspref.append("//pet")

femboygifs = ["https://media.discordapp.net/attachments/921945359243153448/1016475072338341978/attachment.gif",
"https://media.discordapp.net/attachments/921945359243153448/992951022811099206/fuckmedaddyharderohyeailovecokcimsocissyfemboy.gif",
"https://media.discordapp.net/attachments/961748264187748372/996008964129042502/SPOILER_SPOILER_attachment.gif",
"https://cdn.discordapp.com/attachments/929807268994744340/1004411468806107186/F1E8C1FB-2F50-4624-9C10-8BA4E19C1965.gif",
"https://media.discordapp.net/attachments/799634758685425664/987541813810327602/DD136921-EBDA-4D25-BF32-98C37B15EC78.gif",
"https://media.discordapp.net/attachments/949532070366031933/1014903390381281380/togif.gif",
"https://media.discordapp.net/attachments/921945359243153448/1018220255740428470/1D67CB38-444B-4410-B606-C75DB5901087.gif",
"https://cdn.discordapp.com/attachments/753439459005038663/1002532180456648854/lizardplane-1-1-1.gif",
"https://media.discordapp.net/attachments/971267123945029642/1002883399217860608/the.gif",
"https://media.discordapp.net/attachments/946144109620506674/1004050413126942730/364D1F51-B67A-4FA5-83E6-1F32D62B6A78.gif",
"https://media.discordapp.net/attachments/717498714259980378/1001123746452602880/maid_moment.gif",
"https://media.discordapp.net/attachments/717498714259980378/1004768999348916344/reggie_moment.gif",
"https://media.discordapp.net/attachments/717498714259980378/999129608962195466/FUadQMdacAIx8mf-1.gif",
"https://media.discordapp.net/attachments/717498714259980378/993299756682055820/MemeFeedBot-1.gif",
"https://media.discordapp.net/attachments/803872451066593281/992946217430560858/image_2022-03-01_102425.gif",
"https://media.discordapp.net/attachments/717498714259980378/992923755242328136/557BCA7F-B087-4B39-93B1-FF51569624B6.gif",
"https://media.discordapp.net/attachments/717498714259980378/992863130008961167/azarbaijan.gif",
"https://media.discordapp.net/attachments/717498714259980378/989648149029199902/bruhhhh_bruhhhh_bruh-2.gif",
"https://media.discordapp.net/attachments/717498714259980378/989618239631949964/dumbass.gif",
"https://cdn.discordapp.com/attachments/767478105044156472/992836932654604388/boys.gif",
"https://media.discordapp.net/attachments/888278882757795873/955363773080801290/faggot_4.gif",
"https://tenor.com/view/blahaj-go-spinny-blahaj-blahaj-spin-spin-shark-spin-gif-25670993",
"https://tenor.com/view/blahaj-bl%C3%A5haj-ikea-washing-machine-spin-gif-24886740",
"https://media.discordapp.net/attachments/717498714259980378/989579711992713306/femboys3.gif",
"https://media.discordapp.net/attachments/717498714259980378/978426701862297610/aatolfo.gif",
"https://media.discordapp.net/attachments/717498714259980378/976363482033291284/trani.gif",
"https://media.discordapp.net/attachments/381916320423215104/971150129891528794/51CA1BB0-6561-45B1-A3FC-E088E9341F44.gif",
"https://media.discordapp.net/attachments/439519668819066880/966124913700261888/femboy_thinker.gif",
"https://media.discordapp.net/attachments/398590278404931588/971959236684824608/femboysay2.gif",
"https://media.discordapp.net/attachments/927846902123343972/955659490336866314/IMG_9636.gif",
"https://media.discordapp.net/attachments/717498714259980378/971171448548904990/4E77B54B-4AC1-49A9-91EA-2CE559CF328C.gif",
"https://cdn.discordapp.com/attachments/760912627450511369/959259861684715530/ahahahhahahah.gif",
"https://media.discordapp.net/attachments/717498714259980378/971127493308317766/chokeplay-1.gif",
"https://tenor.com/view/sploot-speech-bubble-gif-25277146",
"https://media.discordapp.net/attachments/918199100074258513/986881893083516938/attachment.gif",
"https://media.discordapp.net/attachments/749883971411640390/971733212365725727/you_.gif",
"https://media.discordapp.net/attachments/470168157148020756/961545798963822622/image2.gif",
"https://tenor.com/view/felix-re-zero-felix-argyle-speech-bubble-speech-gif-25397116",
"https://media.discordapp.net/attachments/717498714259980378/970401574390231120/soy.gif",
"https://media.discordapp.net/attachments/398590278404931588/942920201681387570/image0-2.gif",
"https://media.discordapp.net/attachments/717498714259980378/945862747529310268/D2150F09-62F9-48EC-A8BA-775110639806.gif",
"https://media.discordapp.net/attachments/427911040202702858/968228384234696795/adma.gif",
"https://cdn.discordapp.com/attachments/921945359243153448/1026175376621318225/0F62AED4-A79E-48EF-91EB-F3843ABE5C1E.gif",
"https://cdn.discordapp.com/attachments/921945359243153448/1026175377183342642/8583DC0C-0F0A-4592-B4C4-137607AFD3E9.gif",
"https://cdn.discordapp.com/attachments/921945359243153448/1026175377695051806/8BBF99C3-A81E-41C9-9A64-C2F2CEFA2785.gif",
"https://cdn.discordapp.com/attachments/921945359243153448/1026175378395496468/58810059-FF04-4C7A-B5B6-1B67D3FF2956.gif",
"https://media.discordapp.net/attachments/954960957300428812/1021912392571035718/attachment-1.gif",
"https://media.discordapp.net/attachments/945074161611599932/1025184551506542592/448B20AC-A3B8-4026-BC33-90649AAE8216.gif",
"https://media.discordapp.net/attachments/954960957300428812/1019897998374875136/attachment-6.gif",
"https://media.discordapp.net/attachments/993250091328606268/996508965250797618/fun.gif",

]
CHANNEL_MENTION_PATTERN = re.compile('<#(\\d+)>')
EMOJI_PATTERN = re.compile('<:[^:]+?:(\\d+)>')
USER_MENTION_PATTERN = re.compile('<@(\\d+)>')
ROLE_MENTION_PATTERN = re.compile('<@&(\\d+)>')

def returnIQ(iqFLOAT):
    match iqFLOAT:
        case x if x<=1:
            return("HOW THE FUCK ARE YOU SO DUMB??? YOUR IQ IS LITERALLY LESS THAN THE IQ OF A FUCKING SNAIL!\nhttps://tenor.com/view/brainlet-windmill-gif-20767515")
        case x if 1<x<=30:
            return("Okay, listen\nyou either got out of the womb too early... **or**\nyou ate cement, somehow (you really enjoyed it, huh?) <:trolley:987681249759989780>\nhttps://tenor.com/view/soylent-wojak-soy-shocked-meme-what-gif-17036428")
        case x if 30<x<=60:
            return("You seem to be... interesting?\nWho am I kidding, you are a cow, yes! You are cow! You have the IQ of a cow!!!\nhttps://tenor.com/view/pyrocynical-pyro-reaction-live-pyro-reaction-gif-25816788")
        case x if 60<x<=100:
            return("Hm? An average US citizen? Go on, nothing interesting here.\nhttps://tenor.com/view/sfm-soldier-tf2-meme-american-gif-24728385")
        case x if 100<x<=110:
            return("You are world average. Really, you are smarter than the average person in the US, which is a **really positive thing**.\nhttps://tenor.com/view/nintendo-switch-baahh-tada-hi-gif-12601447")
        case x if 110<x<=120:
            return(f"I'm guessing you are proud of your iq ({iqFLOAT}) and probably brag about being atheist or watching *Rick and Morty*.\n**OR...**\nYou are an upstaning citizen and go to a good school/job. In that case I'm proud of ya.\nhttps://tenor.com/view/soy-soy-boy-soy-rage-mad-beta-gif-16525800")
        case x if 120<x<=150:
            return("Hey there smart fella, how ya doing? Having a good day? I hope so...\nhttps://media.discordapp.net/attachments/443853760176062475/839537384043708446/759040029724639252.gif")
        case x if 150<x<300:
            return("Oh WOW\nYOU HAVE impossibly high IQ. Yeah it's just not possible, sorry.\n*Unless you really are smarter than someone more important...*\nhttps://tenor.com/view/intruder-epico-pains-of-hell-wellness-clinic-gif-23860651")
        case x if 300<=x<=400:
            return("OH WHAT THE HELL? YOU **ARE SMARTER THAN DR. ROBOTNIK???** You truly are the smartest.\nhttps://tenor.com/view/puffer-fish-panic-gif-24690452")
        case x if 400<x:
            return("What, are you serious? I think this random number function ``random.uniform()`` went to shit...\nhttps://media.discordapp.net/attachments/800523539605225493/1019993704779493426/Card.gif")
        case _:
            return("idk, something brokie")


regex = r'('

# Scheme (HTTP, HTTPS, FTP and SFTP):
regex += r'(?:(https?|s?ftp):\/\/)?'

 # www:
regex += r'(?:www\.)?'

regex += r'('

 # Host and domain (including ccSLD):
regex += r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+)'

 # TLD:
regex += r'([A-Z]{2,6})'

 # IP Address:
regex += r'|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

regex += r')'

 # Port:
regex += r'(?::(\d{1,5}))?'

 # Query path:
regex += r'(?:(\/\S+)*)'

regex += r')'

def get_emote(emoji):
    """
    Gets a specific emote by lookup.
    :param emoji: The emote to get.
    :type emoji: str or discord.Emoji
    :return:
    :rtype: (str, int)
    """
    lookup, eid = emoji, None
    if ':' in emoji:
        # matches custom emote
        server_match = re.search(r'<a?:(\w+):(\d+)>', emoji)
        # matches global emote
        custom_match = re.search(r':(\w+):', emoji)
        if server_match:
            lookup, eid = server_match.group(1), server_match.group(2)
        elif custom_match:
            lookup, eid = custom_match.group(1), None
        else:
            lookup, eid = emoji.split(':')
        try:
            eid = int(eid)
        except (ValueError, TypeError):
            eid = None
    return eid

translator = googletrans.Translator()
#import dotenv
#NOT USING THIS FUCK THIS LMAO
#from dotenv import load_dotenv
RE_TEST = re.compile('sex', re.IGNORECASE)
#global shitter
#shitter = 0
objectF = type('', (), {})()
bufferMN = type('', (), {})()
imagedata = type('', (), {})()
shitpostermode = type('', (), {})()
reactionmode = type('', (), {})()
#Bot = type('',(),{})()
reactionmode.value = True
shitpostermode.value = False
imagedata.value = None
bufferMN.value = ""
objectF.value = 80
def bufferMImportVaule(stringV, boolV):
    if boolV:
        return bufferMN.value
    else:
        bufferMN.value = stringV
def ShitpostingMode(InputVV, read):
    if read:
        return shitpostermode.value
    else:
        shitpostermode.value = InputVV
def ReactionMode(InputVV, read):
    if read:
        return reactionmode.value
    else:
        reactionmode.value = InputVV
def AttRead(inputV, boolV):
    if boolV:
        return imagedata.value
    else:
        imagedata.value = inputV

def incrementValueInObject(objectF):
    objectF.value = objectF.value + 1
def IfInString(String, SubstringList, CaseSens=True):
    if CaseSens:
        return any(x in String for x in SubstringList)
    else:
        return any(x.lower() in String.lower() for x in SubstringList)
        
#load_dotenv() //FUCK THIS LMAO
TOKEN = os.getenv("DISCORDTOKEN")
intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = setprefix, activity=discord.Activity(type=discord.ActivityType.playing, name="GNU C Compiler"), intents=intents)

@client.event
async def on_ready(): 
    print('Logged in as: {}'.format(client.user))
    #await client.get_channel(921945359243153448).send(f"Morning message will be sent at this timestamp:\n``{str((now + timedelta( seconds= ((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)) )).replace(microsecond=0))}``")
    morning_msg.start()

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    #print(msg.content)
    if msg.content.strip() == "<@444785578152558592>": ##"<@1026940282278776954>":
        #msg.reply("https://media.discordapp.net/attachments/959447085269266442/1003714243599794336/ezgif.com-gif-maker_6.gif")
        await msg.reply("https://cdn.discordapp.com/attachments/949532070366031933/1026944893601447967/caption.gif")
    if re.search("https://media.discordapp.net/attachments/949532070366031933/1026944893601447967/caption.gif", msg.content, re.IGNORECASE):
        print("triggered")
        await msg.reply(f"{msg.author} has le ping ponged Nikki <@444785578152558592>")

    if ShitpostingMode("", True):
        if re.search("deez", msg.content, re.IGNORECASE) or re.search("these", msg.content, re.IGNORECASE): #or re.search("dess", msg.content, re.IGNORECASE):
            await msg.reply("deez nuts in your mouth hah gottem <:trolley:987681249759989780>", mention_author=True)
        if re.search("femboy", msg.content, re.IGNORECASE) or re.search("fem boy", msg.content, re.IGNORECASE) or re.search("fem boi", msg.content, re.IGNORECASE) or re.search("femboi", msg.content, re.IGNORECASE): #or re.search("dess", msg.content, re.IGNORECASE):
            await msg.reply(femboygifs[random.randrange(0,len(femboygifs)-1)], mention_author=True)
        if re.search("lick my", msg.content, re.IGNORECASE) or re.search("ligma", msg.content, re.IGNORECASE):
            await msg.reply("https://tenor.com/view/ligma-balls-gif-22082587", mention_author=True)#https://cdn.discordapp.com/attachments/941621893436424242/1026098045164732496/unknown.png
        if re.search("finger", msg.content, re.IGNORECASE) or re.search("kid named", msg.content, re.IGNORECASE):
            await msg.reply("Kid named Finger:\nhttps://media.discordapp.net/attachments/921945359243153448/994396258611511446/finger.gif", mention_author=True)#https://cdn.discordapp.com/attachments/941621893436424242/1026098045164732496/unknown.png
        if re.search("sex", msg.content, re.IGNORECASE):
            #await msg.reply("HOLY SHIT!!!! YOU SAID THE S*X WORD!!!! :bangbang: :bangbang: :interrobang: :moyai:\nI AM PINGING THE OWNER RIGHT NOW!!!!!!!!! :bangbang: :bangbang:") ##("<@463162198181806082>")
            await msg.reply("https://cdn.discordapp.com/attachments/921945359243153448/1028700825314394162/sex.png")
        if "@" not in msg.content:
            if 'i am ' in msg.content.lower():
                await msg.reply('Hi '+msg.content[msg.content.lower().index('i am ')+5:len(msg.content)]+' I\'m Dad')
            if 'i\'m ' in msg.content.lower():
                await msg.reply('Hi '+msg.content[msg.content.lower().index('i\'m ')+4:len(msg.content)]+' I\'m Dad')
            if 'im ' in msg.content.lower():
                if msg.content.lower().index('im ') == 0 or msg.content[msg.content.lower().index('im ')-1] == ' ':
                    await msg.reply('Hi '+msg.content[msg.content.lower().index('im ')+3:len(msg.content)]+' I\'m Dad')

    if ReactionMode("", True):
        if IfInString(msg.content, ["tree","wise","stablo","euiucet","mystical"],False):
            await msg.add_reaction("<:wisetree:1032609860023504926>")
        try:
            if discord.utils.get(msg.guild.roles, id=1029465397935747243) in msg.author.roles:
                await msg.add_reaction("🐴")
        except:
            #print(f"{msg.content}, {msg.author};;;; This is not a user.")
            pass
            #await msg.reply("This message fucked up role lookup, what the fuck?\n<@444785578152558592>")
        if IfInString(msg.content,["ussy"],False) and not IfInString(msg.content,["sussy"],False):
            await msg.add_reaction("<:no:959662553787682827>")
            await msg.add_reaction("<:manface:1001986026509697144>")
        elif "sussy" in msg.content.lower():
            match random.randint(1, 2):
                case 1:  
                    await msg.add_reaction("<:amogus:930915078516117625>")
                case 2:
                    await msg.add_reaction("<:among:1001086237643386911>")
                    await msg.add_reaction("<:us:1001086258493263912>")
        if IfInString(msg.content,["<:flag_bi:942435468455342090>","🏳️‍🌈","🏳️‍⚧️","gay","homosexual","bisexual","transgender"],False):
            await msg.add_reaction(random.choice(["<:flag_bi:942435468455342090>","🏳️‍🌈","🏳️‍⚧️"]))
        if IfInString(msg.content,["akshually","nerd","🤓"],False):
            await msg.add_reaction("🤓")
        if "https://tenor.com/view/matrix-the-agents-know-dont-gif-18536773" in msg.content:
            if msg.reference:
                await msg.reference.resolved.reply("https://tenor.com/view/matrix-the-agents-know-dont-gif-18536773")
            else:
                await msg.channel.send("https://tenor.com/view/matrix-the-agents-know-dont-gif-18536773")

    
    if msg.attachments != [] and msg.content.startswith(tuple(petaliaspref)):
        AttRead([msg.attachments[0].url, msg.id], False)
    if msg.content.lower().startswith("replytest") and msg.author != client.user and msg.reference:
        if msg.reference.resolved:
            print(msg.reference.resolved.content)
            await msg.reply(f"raw content: ``{msg.reference.resolved.content}``")
        else:
            await msg.channel.send("Something went wrong: ln 45")

 
    if msg.content.lower().startswith("pls translate"):
        global bufferM
        if msg.author != client.user and msg.reference:
            if msg.reference.resolved:
                bufferMImportVaule(msg.reference.resolved.content, False)
            else:
                await msg.channel.send("Something went wrong: ln 53")
                return
        else:
            bufferMImportVaule(msg.content[len("pls translate")+1:], False)
        bufferM = bufferMImportVaule("", True)
        if "@everyone" in bufferM or "@here" in bufferM:
            await msg.channel.send("Absolutely fucking **NOT** doing that.")
            return
        if "@" in bufferM:
            #await msg.channel.send("Pls remove le funny ``@`` from your nick input. Thanks")
            bufferM = bufferM.replace("@","<At>")
        #print(f"{bufferM}, {type(bufferM)}")
        #print(translator.detect(bufferM).lang)
        message_destination = translator.detect(bufferM).lang #TODO: add lang filter 
        print(message_destination)
        if type(message_destination) == list:
            message_destination = random.choice(message_destination)
        if message_destination == "en":
            await msg.channel.send("Your requested text for translation is already in english!")
            return
        translated_message = translator.translate(bufferM,src=message_destination, dest="en")
        returned_nation = getNation(message_destination)
        flagbuf = flag.flag(returned_nation) if returned_nation != None else "``[no flag]``"
        await msg.channel.send(f"``{bufferM}`` -> ``{translated_message.text}``, translation invoked by **{msg.author}**.\nLanguage flags: {flagbuf} | ``{message_destination}`` ->  🇺🇸 | ``en-us``")#.format(bufferM, translated_message.text, msg.author, message_destination, "en"))
        return
        
    await client.process_commands(msg)

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar_old(ctx, member:discord.Member = None):
    member = ctx.author if not member else member
    userAvatarUrl = member.avatar.url
    embed=discord.Embed(title=f"{member.name}'s Avatar")
    embed.set_image(url=f'{userAvatarUrl}')
    await ctx.send(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "📌" and discord.utils.get(reaction.message.guild.roles, id=941621150293843979) in user.roles:
        print(reaction.message)
        await reaction.message.pin()


@client.event
async def on_reaction_remove(reaction, user):
    if reaction.emoji == "📌" and discord.utils.get(reaction.message.guild.roles, id=941621150293843979) in user.roles:
        if not ":pushpin:" in [ reaction.emoji for reaction in  reaction.message.reactions]:
            print(reaction.message)
            await reaction.message.unpin()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown for {round(error.retry_after, 2)} more seconds.')
    else:
        print(error)


@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def pussy(ctx, member:discord.Member = None):
    if not ShitpostingMode("", True):
        await ctx.reply(f"This command is disabled due to shitposting mode being set to ``{ShitpostingMode('',True)}``")
        return
    member = ctx.author if not member else member
    rand_depth = random.uniform(1, 30)
    depth_inches = rand_depth * 0.393701
    mesg = f"pussy depth is {round(rand_depth, 2)}cm / {round(depth_inches, 2)} inches deep! <:trolley:987681249759989780>"
    print(mesg)
    await ctx.channel.send(f"Result: {member.name}'s {mesg}")

@client.command(pass_context=True)
##@commands.has_permissions(administrator=True)

##TODO: Fix this trashy version of clear: add int type checking n stuff
##async def clear(ctx, limit: int=None):
##    if type(limit) != int:
##        await ctx.reply(f"That can't work, right? You can't clear an invalid amount of messages!")
##        return
##    if ctx.author.id == 444785578152558592:
##        if limit <= 0:
##            await ctx.reply(f"That can't work, right? You can't clear ``{limit}`` messages!")
##            return
##        await ctx.channel.purge(limit=limit)
##        await ctx.send(f'{limit} messages have been cleared by {ctx.author.name}.')
##        await ctx.message.delete()
##    else:
##        await ctx.reply("https://tenor.com/view/rat-toilet-mouse-toiler-ew-gif-21327850")

async def clear(ctx, amount = "0"):
    if ctx.author.id == 444785578152558592:
        pass
    else:
        await ctx.reply("https://tenor.com/view/rat-toilet-mouse-toiler-ew-gif-21327850")
        return
    if amount == "all":
        await ctx.channel.purge(limit=50)
        await ctx.send("Cleared the entire chat!")
        print("Cleared the chat!")
    else :
        try:
            amount = int(amount)
        except ValueError:
            await ctx.reply(f"That can't work, right? You can't clear an invalid amount of messages!", delete_after=5)
            return
        if amount <= 0:
            await ctx.reply(f"That can't work, right? You can't clear ``{amount}`` messages!", delete_after=5)
            return
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Done!\n{amount} messages have been cleared by {ctx.author.name}!", delete_after=5)
        print(f'``{amount}`` messages have been cleared by {ctx.author.name}.')



@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def bussy(ctx, member:discord.Member = None):
    if not ShitpostingMode("", True):
        await ctx.reply(f"This command is disabled due to shitposting mode being set to ``{ShitpostingMode('',True)}``")
        return
    member = ctx.author if not member else member
    rand_depth = random.uniform(1, 50)
    depth_inches = rand_depth * 0.393701
    mesg = f"bussy depth is {round(rand_depth, 2)}cm / {round(depth_inches, 2)} inches deep! :flushed::weary:"
    print(mesg)
    await ctx.channel.send(f"Result: {member.name}'s {mesg}")

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def iqtest(ctx, member:discord.Member = None):
    if not ShitpostingMode("", True):
        await ctx.reply(f"This command is disabled due to shitposting mode being set to ``{ShitpostingMode('',True)}``")
        return
    member = ctx.author if not member else member
    rand_depth = random.uniform(1, 300)
    rand_depth2 = random.uniform(0.2, 2)
    xff = round(rand_depth*rand_depth2, 2)
    if member.id == 444785578152558592:
        xff = 500
    elif member.id == 371425463060398090:
        xff= 70
    mesg = f"IQ is {xff}"
    print(mesg)
    await ctx.channel.send(f"Result: {member.name}'s {mesg}.\n{returnIQ(xff)}")

@client.command()
async def avatar(ctx, avamember: discord.Member = None):
    if avamember == None:
        member = ctx.author if not avamember else avamember
        userAvatarUrl = member.avatar.url
        embed = discord.Embed(title=('{}\'s Avatar'.format(member.name)), colour=discord.Colour.red())
        embed.set_image(url='{}'.format(userAvatarUrl))
        await ctx.reply(embed=embed, mention_author=True) 
    else:
        userAvatarUrl = avamember.avatar.url
        embed = discord.Embed(title=('{}\'s Avatar'.format(avamember.name)), colour=discord.Colour.red())
        embed.set_image(url='{}'.format(userAvatarUrl))
        await ctx.reply(embed=embed, mention_author=True) 


@client.command(pass_context=True, aliases=petalias)
async def pet(ctx, thing: str = ""):
    print(type(thing))
    print(AttRead("", True))
    if AttRead("", True) == None:
        AttRead(["",0], False)
    #print(ctx.attachments == [])
    #print(ctx.attachments)
    try:
        print(re.compile(regex, re.IGNORECASE).search(thing).group(0).strip())
        itworks = True
    except:
        print("eh whatever")
        itworks = False
        pass
    #print(f"{type(thing)};; {thing}")
    #print(USER_MENTION_PATTERN.findall(thing))
    if bool(re.match(EMOJI_PATTERN, thing)):
        #print(type(EMOJI_PATTERN.findall(thing)))
        buf = (int(EMOJI_PATTERN.findall(thing)[0]))
        #print("fuckup 1")
        url = buf
        #print(url)
        if not url:
            await ctx.reply('Please use a custom emoji, image or tag a member to petpet their avatar!')
            return
        response = requests.get(f"https://cdn.discordapp.com/emojis/{url}.webp")
    elif bool(re.match(USER_MENTION_PATTERN, thing)):
        #print("hello")
        a = (int(USER_MENTION_PATTERN.findall(thing)[0]))
        zf = client.get_user(a)
        buf = a
        url = zf.avatar.url 
        response = requests.get(url)
    elif AttRead("", True)[1] == ctx.message.id: ##TODO: Dodaj ctx provjeru za korisnika tako da je attread jednak ctx.id
        buf = ctx.author.id
        url = AttRead("", True)[0]
        response = requests.get(url)

    elif itworks:
        find_urls_in_string = re.compile(regex, re.IGNORECASE)
        urlBF = find_urls_in_string.search(thing)
        try:
            #url = 
            if urlBF.group(0).strip().endswith(">"): url = urlBF.group(0).strip()[:-1]
            else: url = urlBF.group(0).strip()
            buf = urlBF.group(3).strip()
            response = requests.get(url)
        except:
            await ctx.reply('Given link does not contain a file or image <:trolley:987681249759989780>')
            return
#    elif ctx.attachment and type(thing) != None:
#        url = message.attachments[0].url
#        buf = ctx.author.id
    else:
        await ctx.reply('Please use a custom emoji, image or tag a member to petpet their avatar!')
        return

    source = BytesIO(response.content) # file-like container to hold the emoji in memory
    dest = BytesIO() # container to store the petpet gif in memory
    try:
        petpetgif.make(source, dest)
    except:
        await ctx.reply('Conversion to image failed, probablly bcus the input was **NOT an image**')
        return
    dest.seek(0) # set the file pointer back to the beginning so it doesn't upload a blank file.
    await ctx.reply(file=discord.File(dest, filename=f"{buf}-petpet.gif"))

@client.command()
async def clussy(ctx):
    if not ShitpostingMode("", True):
        await ctx.reply(f"This command is disabled due to shitposting mode being set to ``{ShitpostingMode('',True)}``")
        return
    embed=discord.Embed(title=f"{ctx.author} IS A FUCKING CLOWN!", description="LOOK AT THIS FUCKING CLOWN, THIS PERSON IS SO ADDICTED TO PORN THAT NORMAL CATEGORIES ARE NOT ENOUGH!!!")
    #embed=discord.Embed("")
    embed.set_image(url=f'https://media.tenor.com/MW1mSw50oK0AAAAC/clown-clown-meme.gif')
    await ctx.reply(embed=embed, mention_author=True)

@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    print(ctx.message.author.id)
    if ctx.message.author.id != 444785578152558592:
        await ctx.reply("Nope, blocked + ratio + cope + seethe + mald + you lose + no admin + trolled + no bitches")
        return
    if len(nick) >= 32:
        await ctx.reply("Nick too long <:pipe:997026453952671834>")
        return
    await member.edit(nick=nick)
    await ctx.reply(f'Nickname was changed for {member.name} <:letrollface:972002906041626635>')


@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def botname(ctx):
    if not ShitpostingMode("", True):
        await ctx.reply(f"This command is disabled due to shitposting mode being set to ``{ShitpostingMode('',True)}``")
        return
    nick = ctx.message.content[len("botname")+3:]
    if len(nick) >= 32:
        await ctx.reply("Nick too long <:pipe:997026453952671834>")
        return
    if "@everyone" in nick or "@here" in nick:
        await ctx.reply("Absolutely fucking **NOT** doing that.")
        return
    if "@" in nick:
        await ctx.reply("Pls remove le funny ``@`` from your nick input. Thanks")
        return
    await ctx.message.guild.me.edit(nick=nick)
    await ctx.reply(f'Bot nick was changed to **{nick}** by {ctx.author} <:letrollface:972002906041626635>')#

#@client.command(pass_context=True)
#async def getpfp(ctx):
#    if ctx.message.author.id != 444785578152558592:
#        await ctx.reply("Nope, blocked + ratio + cope + seethe + mald + you lose + no admin + trolled + no bitches")
#        return
#    await ctx.reply("Finding this specified pfp:\nhttps://cdn.discordapp.com/attachments/967479617734705153/1032350270119751741/unknown.png")
#    for i in ctx.guild.members:
#        try:
#            ffb = imagecomparison.imagematch(f"{i.avatar.url}")
#            print(ffb, i)
#            if ffb[1] > 0.40:
#                print(f"found match!!!!!!!!!!!!!!!!!!!!!!!!!!! {i}")
#                await ctx.author.send(f"Perhaps a match?, {i} , {i.avatar.url}")
#        except:
#            await ctx.author.send(f"Uh oh, something went wrong for user {i}, couldn't fetch their image.")
#        time.sleep(1)
#    ctx.reply("Image search complete!")
#    #print(imagecomparison.imagematch(f"{ctx.author.avatar.url}"))


@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def shitter(ctx):
    if not ShitpostingMode("", True):
        await ctx.reply(f"This command is disabled due to shitposting mode being set to ``{ShitpostingMode('',True)}``")
        return
#    incrementValueInObject(objectF)
#    await ctx.reply(f"<@{ctx.message.author.id}> shits on {random.choice(ctx.guild.members).mention}. Total shits: {objectF.value}")
    await ctx.reply("Yeah I'm fucking done with this, later bitchesssss")

##@commands.cooldown(1, 1, commands.BucketType.user)
@client.command(pass_context=True)
async def toggleshit(ctx):
    if ctx.message.author.id != 444785578152558592:
        await ctx.reply("This command exists with a reason, you know what happens when people spam the bot.")
        return
    ShitpostingMode(not ShitpostingMode("", True), False)
    await ctx.reply(f"Shitposting mode has been set to ``{ShitpostingMode('',True)}``")

@client.command(pass_context=True)
async def togglereactions(ctx):
    if ctx.message.author.id != 444785578152558592:
        await ctx.reply("This command exists with a reason, reactions can get messy...")
        return
    ReactionMode(not ReactionMode("", True), False)
    await ctx.reply(f"Reactions have been set to ``{ReactionMode('',True)}``")

@client.command(aliases=["mcrnow"])
async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)

@tasks.loop(count=None,)
async def morning_msg():
    print(((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)))
    #await asyncio.sleep((timedelta(hours=24) - (now - now.replace(hour=18, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600))
    #await client.get_channel(921945359243153448).send("Current time is exactly 6:00PM")
    await asyncio.sleep((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600))
    await client.get_channel(921945359243153448).send("https://media.discordapp.net/attachments/921945359243153448/1033764795557609662/europe.jpg")


#@client.event
#async def on_error(event, *args, **kwargs):
#    message = args[0] #Gets the message object
#    logging.warning(traceback.format_exc()) #logs the error
#    await client.send_message(message.channel, "Error encoutnered, report to dev (Uru)!!\nhttps://tenor.com/view/computer-smash-rage-flash-gif-19862483") #send the message to the channel
#bot = client
client.lavalink_nodes = [
#{"host": "lv.cowcat.cf", "port": 2223, "password": "derpylava", "https": False},
    {"host": "lavalink.botsuniversity.ml", "port": 443, "password": "mathiscool", "https": True },
    {"host": "lavalink2.botsuniversity.ml", "port": 443, "password": "mathiscool", "https": True },
    {"host": "node2.lewdhutao.tech", "port": 443, "password": "lewdhutao", "https": True },
]
client.spotify_credentials = {
    'client_id': '905fab4830e44104b41a5ffe03ee695f',
    'client_secret': '696fa36e81824c00a401b70fb7744315'
}
client.load_extension('dismusic')
client.run(TOKEN)
#https://media.tenor.com/MW1mSw50oK0AAAAC/clown-clown-meme.gif
