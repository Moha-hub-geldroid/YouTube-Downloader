#imports 
import telebot
from prettytable import PrettyTable 
from pytube import YouTube
import os
import requests

###################################################################


bot = telebot.TeleBot("5833750101:AAEF4r6FTnHarUvwjBF7PNdQ7v1X10Oa6CQ")

# start message 
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text = "Welcome To YouTube Downloader\n\nOwner: @sirr_b52")

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

@bot.message_handler(commands=["youtube"])
def youtube_downloader(message):
    link = message.text.replace("/yotube","")
    try:
        video = YouTube(link)
        title = video.title
        video.streams.filter(progressive=True, file_extension='mp4')
        vide = video.streams.get_highest_resolution().download(filename="Downloaded_by_sirr_b52.mp4")
        vid = open(vide,'rb')
        bot.send_video(message.chat.id,video=vid)
        bot.reply_to(message,"Download completed Successfully !\nvideo title : {}\nvideo views : {}\nBy : @sirr_b52".format(video.title,video.views))
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
        audio.streams.filter(progressive=True , file_extension='mp3')
        audi = audio.streams.get_highest_resolution().download(filename="Downloaded_by_sirr_b52.mp3")
        aud = open(audi,'rb')
        bot.send_document(message.chat.id,aud)
        bot.reply_to(message,"Download completed Successfully !\nvideo title : {}\nvideo views : {}\nBy : @sirr_b52".format(audio.title,audio.views))
        aud.close()
        os.remove("Downloaded_by_sirr_b52.mp3")
    except:
        bot.send_message(message.chat.id,text="There is nothing to download !!")


bot.polling()
