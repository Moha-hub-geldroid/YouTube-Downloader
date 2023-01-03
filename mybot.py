# coded by Mohammad Mhaidat
# instagram : sirr.b52
# social media's telegram bot downloader


#imports 
import telebot
from prettytable import PrettyTable 
from pytube import YouTube
import os
import requests
import json


bot = telebot.TeleBot("5630845902:AAFMvezKk09GXt5T4rzXW6G6o_BpUN1Y8Eg")

# start message 
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text = "Welcome To YouTube Downloader\n\nOwner: @sirr_b52")
@bot.message_handler(commands=["commands"])
def commands(message):
    bot.send_message(message.chat.id,text="/start ==> getting start with this bot !\n\n/help ==> to get help in how to use this bot\n\n/commands ==> to show all commands \n\n/youtube_help ==> to get help in how to use youtube tools\n\n/youtube <VIDEO LINK> ==> to download a youtube video 'mp4 extension'\n\n/youtube_audio <VIDEO LINK> ==> to download youtube video's audio 'mp3 extension'\n\n/instagram ==> download any instagram video or photo\n\n/instagram_help ==> to get help in how to use instagram tool\n\n/tiktok ==> download any tiktok video without watermark\n\n/tiktok_audio <YOUR LINK> ==> download tiktok video's audio 'mp3'\n\n/tiktok_help <YOUR LINK> ==> to get help in how to use tiktok tools")
    bot.send_message(message.chat.id,text="*Important notice :* _<YOUR LINK>_  means enter your link *without* <> tags",parse_mode="markdown")
    
    
# help function
@bot.message_handler(commands=["help"])
def help(message):
    help = PrettyTable()
    help.field_names = ["SITE","COMMAND"]
    help.add_row(["YouTube","/youtube_help"])
    help.add_row(["Instagram","/instagram_help"])
    help.add_row(["Tiktok","/tiktok_help"])
    bot.send_message(message.chat.id,text=str(help))


@bot.message_handler(commands=['youtube_help'])
def youtube_help(message):
    youtube_table = PrettyTable()
    youtube_table.field_names = ["USAGE","METHOD","EXTENSION"]
    youtube_table.add_row(["audio","/youtube_audio","mp3"])
    youtube_table.add_row(["video","/youtube","mp4"])
    bot.send_message(message.chat.id,text=str(youtube_table))
    bot.send_message(message.chat.id,text="Example : /youtube https://www.example.com/test\n\n*Important notice :* _<YOUR LINK>_  means enter your link *without* <> tags",parse_mode="markdown")


@bot.message_handler(commands=["youtube"])
def youtube_downloader(message):
    link = message.text.replace("/yotube","")
    try:
        video = YouTube(link)
        title = video.title
        length = str(int(audio.length/60))+":"+str(audio.length%60)
        video.streams.filter(progressive=True, file_extension='mp4')
        vide = video.streams.get_highest_resolution().download(filename="Downloaded_by_sirr_b52.mp4")
        vid = open(vide,'rb')
        bot.send_video(message.chat.id,video=vid)
        bot.reply_to(message,"Download completed Successfully ✅\n➡️video title : {}\n➡️video views : {}\n➡️video length : '{}' minutes\n\nBy : @sirr_b52".format(video.title,video.views,length))
        vid.close()
        os.remove("Downloaded_by_sirr_b52.mp4")
        print("success")
    except:
        bot.send_message(message.chat.id,text="There is nothing to download !!")
@bot.message_handler(commands=["youtube_audio"])
def yotube_audio_downloader(message):
    link= message.text.replace("/youtube_audio","")
    try:
        audio = YouTube(link)
        length = str(int(audio.length/60))+":"+str(audio.length%60)
        audio.streams.filter(progressive=True , file_extension='mp3')
        audi = audio.streams.get_highest_resolution().download(filename="Downloaded_by_sirr_b52.mp3")
        aud = open(audi,'rb')
        bot.send_document(message.chat.id,aud)
        bot.reply_to(message,"Download completed Successfully ✅\n➡️video title : {}\n➡️video views : {}\n➡️video length : '{}' minutes\n\nBy : @sirr_b52".format(audio.title,audio.views,length))
        aud.close()
        os.remove("Downloaded_by_sirr_b52.mp3")
    except:
        bot.send_message(message.chat.id,text="There is nothing to download !!")



@bot.message_handler(commands=["instagram"])
def instagram(message):
    
    try:
        url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"
        postUrl = message.text.replace("/instagram ","")
        print(postUrl)
        headers = {
        'x-rapidapi-host': "instagram-media-downloader.p.rapidapi.com",
        'x-rapidapi-key': "3e4a585b37msh0d5d14130a89f2ap10380ajsnca63527f890b" # Put Your API Key 
        }
        querystring = {"url": postUrl}

        response = requests.request("GET", url, headers=headers, params=querystring)

        textToJson = json.loads(response.text)

        postFileUrl = ''

        if 'video' in textToJson:
            postFileUrl = textToJson["video"]
        else:
            postFileUrl = textToJson["image"]

        reqPostFileUrl = requests.get(postFileUrl)

        fileEx = reqPostFileUrl.headers['Content-Type'].split('/')[-1].split('.')[0]
        filename_ = "downloaded by sirr_b52."+str(fileEx)
        with reqPostFileUrl as rq:
            with open(filename_, 'wb') as file:
                file.write(rq.content)
        botfile = open(filename_,'rb')
        bot.send_document(message.chat.id,botfile)
        botfile.close()
        bot.reply_to(message,"Post downloaded successfully ✅")
    except:
        bot.reply_to(message,text="Sorry .. I cant download this type of posts ❌")

@bot.message_handler(commands=["instagram_help"])
def instagram_help(message):
    bot.send_message(message.chat.id,text = "command : /instagram *<YOUR LINK>*\n\ncan download *video or image* from instagram",parse_mode="markdown")
    bot.send_message(message.chat.id,text="*Important notice :* _<YOUR LINK>_  means enter your link *without* <> tags",parse_mode="markdown")



@bot.message_handler(commands=["tiktok"])
def tiktok(message):
    link = message.text.replace("/tiktok ","")
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
    querystring = {"url":link}
    headers = {
	"X-RapidAPI-Key": "3e4a585b37msh0d5d14130a89f2ap10380ajsnca63527f890b",
	"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"}
    if "https://" in str(link):
        res = requests.request("GET", url, headers=headers, params=querystring).json()
        entrance = res["originvideo"]
        req = requests.Session().get(entrance).content
        filename = "downloaded by sirr b52.mp4"
        with open(filename,"wb") as file:
            file.write(req)
            file.flush()
        filename_ = open(filename,'rb')
        bot.send_document(message.chat.id,filename_)
        bot.reply_to(message,"Post downloaded successfully ✅")
    else:
        bot.reply_to(message,text="Sorry .. Something went wrong try again later ❌")

@bot.message_handler(commands=["tiktok_audio"])
def tiktok_audio(message):
    link = message.text.replace("/tiktok_audio ","")
    if "https://" in str(link):
        res = requests.Session().get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={link}&key=godownloader.com").json()
        entrance = res["music_url"]
        req = requests.Session().get(entrance).content
        filename = "downloaded by sirr b52.mp3"
        with open(filename,"wb") as file:
            file.write(req)
            file.flush()
        filename_ = open(filename,'rb')
        bot.send_document(message.chat.id,filename_)
        bot.reply_to(message,"Post downloaded successfully ✅")
    else:
        bot.reply_to(message,text="Sorry .. Something went wrong try again later ❌")


@bot.message_handler(commands=["tiktok_help"])
def tiktok_help(message):
    tik_help = PrettyTable()
    tik_help.field_names("USAGE","METHOD","EXTENSION")
    tik_help.add_row("video","/tiktok <YOUR LINK>","mp4")
    tik_help.add_row("audio","/tiktok_audio <YOUR LINK>","mp3")
    bot.send_message(message.chat.id,text=tik_help)
    bot.send_message(message.chat.id,text="Example : /tiktok https://vm.tiktok.com/test\n\n*Important notice :* _<YOUR LINK>_  means enter your link *without* <> tags",parse_mode="markdown")


bot.polling()
