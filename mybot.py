#imports 
import telebot
from telebot import *
from prettytable import PrettyTable 
from pytube import YouTube
import os

###################################################################


bot = telebot.TeleBot("5833750101:AAEF4r6FTnHarUvwjBF7PNdQ7v1X10Oa6CQ")

# start message 
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text = "Welcome To YouTube Downloader\n\nOwner: @sirr_b52")
@bot.message_handler(commands=["commands"])
def commands(message):
    bot.send_message(message.chat.id,text="/start ==> getting start with this bot !\n\n/help ==> to get help in how to use this bot\n\n/commands ==> to show all commands \n\n/youtube_help ==> to get help in how to use youtube tools\n\n/youtube <VIDEO LINK> ==> to download a youtube video 'mp4 extension'\n\n/youtube_audio <VIDEO LINK> ==> to download youtube video's audio 'mp3 extension'")
    
    
# help function
@bot.message_handler(commands=["help"])
def help(message):
    h = PrettyTable()
    h.field_names = ["SITE","COMMAND"]
    h.add_row(["YouTube","/youtube_help"])
    bot.send_message(message.chat.id,text=str(h))


@bot.message_handler(commands=['youtube_help'])
def youtube_help(message):
    youtube_table = PrettyTable()
    youtube_table.field_names = ["USAGE","METHOD","EXTENSION"]
    youtube_table.add_row(["audio","/youtube_audio","mp3"])
    youtube_table.add_row(["video","/youtube","mp4"])
    bot.send_message(message.chat.id,text=str(youtube_table))
    bot.send_message(message.chat.id,text="Example : /youtube https://www.example.com/test")

@bot.message_handler(commands=["youtube"])
def youtube_downloader(message):
    link = message.text.replace("/yotube","")
    try:
        video = YouTube(link)
        title = video.title
        length = video.length/60
        video.streams.filter(progressive=True, file_extension='mp4')
        vide = video.streams.get_highest_resolution().download(filename="Downloaded_by_sirr_b52.mp4")
        vid = open(vide,'rb')
        bot.send_video(message.chat.id,video=vid)
        bot.reply_to(message,"Download completed Successfully !\nvideo title : {}\nvideo views : {}\nvideo length : '{}' minutes\n\nBy : @sirr_b52".format(video.title,video.views,length))
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
        length = audio.length/60
        audio.streams.filter(progressive=True , file_extension='mp3')
        audi = audio.streams.get_highest_resolution().download(filename="Downloaded_by_sirr_b52.mp3")
        aud = open(audi,'rb')
        bot.send_document(message.chat.id,aud)
        bot.reply_to(message,"Download completed Successfully !\nvideo title : {}\nvideo views : {}\nvideo length : '{}' minutes\n\nBy : @sirr_b52".format(audio.title,audio.views,length))
        aud.close()
        os.remove("Downloaded_by_sirr_b52.mp3")
    except:
        bot.send_message(message.chat.id,text="There is nothing to download !!")


bot.polling()
