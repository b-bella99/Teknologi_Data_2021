import os
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
import requests
import weather2_1841720004
import hddspace_1841720004
import steam_1841720004
import news_1841720004
import xplane_1841720004

print(datetime.now().strftime('%A, %d %B %Y\n'))
print("LOADING, PLEASE WAIT..\n")

# create window - resize false - size - title card
root = tk.Tk()
root.resizable(False, False)
root.geometry('1305x780')
root.title("Dashboard")
root.configure(bg='#c7d5e0')

# DRAW TOP BLUE BAR - TITLE _ DATETTIME
top_bg = tk.Canvas(root, width=1305, height=60, bg='#1b2838', highlightthickness=0).place(x=0, y=0)
tk.Label(top_bg, text='Dashboard', font='Montserrat 25', bg='#1b2838', fg='white').place(x=15, y=3)
tk.Label(top_bg, text=datetime.now().strftime('%A, %d %B %Y'), font='Montserrat 20', bg='#1b2838', fg='white').place(
    x=930, y=8)

# BBC NEWS
news_box = tk.Canvas(root, width=350, height=140, bg='#2a475e', highlightthickness=0).place(x=20, y=620)
news_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=600)
tk.Label(news_box_top, text='BBC NEWS', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF').place(x=25, y=600)

news_data = news_1841720004.GetNews()

headline = []
news_y = 620
for i in range(0, 7):
    if len(news_data[i]) > 50:
        headline.append(news_data[i][:50] + '....')
    else:
        headline.append(news_data[i])
    tk.Label(news_box, text='-' + headline[i], font='Montserrat 9', bg='#2a475e', fg='#FFFFFF').place(x=25, y=news_y)
    news_y += 19

# Threshold News
threshold_box = tk.Canvas(root, width=285, height=520, bg='#2a475e', highlightthickness=0).place(x=1000, y=240)
threshold_box_top = tk.Canvas(root, width=285, height=20, bg='#1b2838', highlightthickness=0).place(x=1000, y=220)
tk.Label(threshold_box_top, text='Threshold News', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF').place(x=1005,
                                                                                                               y=220)

threshold_headlines = xplane_1841720004.getheadlines()
print('threshold_headlines')
print(threshold_headlines)


def getimage_threshold(imgurl):
    response_img = requests.get(imgurl)
    img_data = response_img.content
    img_resize = Image.open(BytesIO(img_data)).resize((245, 120), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_resize)
    return img


th_y = 255
threshold_list = []
print
for i in range(3):
    th_y += 170

# STEAM TOP SELLING
steam_box = tk.Canvas(root, width=590, height=520, bg='#2a475e', highlightthickness=0).place(x=390, y=240)
steam_box_top = tk.Canvas(root, width=590, height=20, bg='#1b2838', highlightthickness=0).place(x=390, y=220)
steam_box_price = tk.Canvas(steam_box, width=80, height=520, bg='#171a21', highlightthickness=0).place(x=900, y=240)
tk.Label(steam_box_top, text='Steam Top Selling', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF').place(x=395,y=220)

steam_games = steam_1841720004.GetGames()

def getimage_steam(imgurl):
    url = 'https://steamcdn-a.akamaihd.net/steam/apps/'+imgurl+'/capsule_184x69.jpg'
    response_img = requests.get(url)
    img_data = response_img.content
    img_resize = Image.open(BytesIO(img_data)).resize((107,40), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_resize)
    return img

img_y = 240
photo_list = []
for i in range(0,13):
    photo_list.append(getimage_steam(steam_games[i].imgurl))
    tk.Label(root, image = photo_list[i], width=107, height=40, bd=0).place(x=390, y=img_y)
    img_y += 40

steam_y = 245
for i in range(0,13):
    tk.Label(steam_box, text=steam_games[i].title, font='Montserrat 12', bg='#2a475e', fg='#FFFFFF').place(x=500, y=steam_y)
    tk.Label(steam_box, text=steam_games[i].price, font='Montserrat 12', bg='#171a21', fg='#FFFFFF').place(x=910,y=steam_y)
    steam_y += 40

# weather
weather_data = weather2_1841720004.get()

weather_box = tk.Canvas(root, width=1265, height=100, bg='#2a475e', highlightthickness=0).place(x=20, y=100)
weather_box_top = tk.Canvas(root, width=1265, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=80)
tk.Label(weather_box_top, text='Weather Forecast, York UK', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF').place(x=25, y=80)

def geticon_weather(iconcode):
    url = 'http://openweathermap.org/img/wn/' + iconcode + '@2x.png'
    response_img = requests.get(url)
    img_data = response_img.content
    img_resize = Image.open(BytesIO(img_data)).resize((80,80), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_resize)
    return img

day_x = 165
icon_x = 150
icon_list = []
for i in range(0, 8):
    icon_list.append(geticon_weather(weather_data[0][i].icon))
    tk.Label(root, image=icon_list[i], width=80, height=80, bd=0, bg='#2a475e').place(x=icon_x, y=100)
    tk.Label(root, text=weather_data[0][i].day + '-' + str(weather_data[0][i].temp) + '°', bg='#2a475e', fg='#FFFFFF', font='Montserrat 8').place(x=day_x, y=170)
    icon_x += 120
    day_x += 120

tk.Label(weather_box, text=str(weather_data[0][0].temp) + '°', font='Montserrat 40', bg='#2a475e', fg='#FFFFFF').place(x=50, y=107)
tk.Label(weather_box, text='Sunrise: '+ weather_data[1], font='Montserrat 12', bg='#2a475e', fg='#FFFFFF').place(x=1100, y=120)
tk.Label(weather_box, text='Sunset: '+ weather_data[2], font='Montserrat 12', bg='#2a475e', fg='#FFFFFF').place(x=1105, y=150)

# PI HOLE -----------------------------------------
#pihole_data = piholeget.GetData()
pihole_box = tk.Canvas(root, width=350, height=140, bg='#2a457e', highlightthickness=0).place(x=20, y=240)
pihole_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=220)
pihole_box_temp = tk.Canvas(root, width=350, height=30, bg='#2a457e', highlightthickness=0).place(x=20, y=240)
pihole_box_middle = tk.Canvas(root, width=350, height=20, bg='#171a21', highlightthickness=0).place(x=20, y=270)
tk.Label(pihole_box_top, text='Raspberry Pi Status', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF').place(x=25, y=220)

pihole_enabled_colour = '#E74C3C'

tk.Label(pihole_box_temp, text='Pi Hole - data[0]', font='Montserrat 7 bold', bg='#171a21', fg=pihole_enabled_colour).place(x=25, y=270)

tk.Label(pihole_box, text='Temprature: data[5] °C', font='Montserrat 12 bold', bg='#2a475e',fg='#FFFFFF').place(x=22, y=240)

tk.Label(pihole_box, text='Memory Usage: data[6] %', font='Montserrat 12 bold', bg='#2a475e',fg='#FFFFFF').place(x=220, y=240)

tk.Label(pihole_box, text='Percentage Blocked: data[1]', font='Montserrat 12 bold', bg='#2a475e',fg='#FFFFFF').place(x=25, y=292)

tk.Label(pihole_box, text='Queries Blocked: data[2]', font='Montserrat 12 bold', bg='#2a475e',fg='#FFFFFF').place(x=25, y=320)
tk.Label(pihole_box, text='Last Updated: str(data[3]) days, str(data[4]) hours',font='Montserrat 12 bold', bg='#2a475e',fg='#FFFFFF').place(x=25, y=348)

full_path = os.path.realpath(__file__)
checkmark_image = Image.open(os.path.dirname(full_path)+ "\\images\\checkmark3.png")
checkmark = ImageTk.PhotoImage(checkmark_image)
canvas_checkmark = tk.Canvas(pihole_box, width=77, height=80, bg='#2a475e', bd=0, highlightthickness=0)
canvas_checkmark.create_image(0, 0, image=checkmark, anchor='nw')

# Hard Drive Capacities
hdd_data = hddspace_1841720004.GetDriveSpace()

hdd_box = tk.Canvas(root, width=350, height=160, bg='#2a475e', highlightthickness=0).place(x=20, y=420)
hdd_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=200)
tk.Label(hdd_box_top, text='Current Hard Drive Capacities', font='Montserrat 7 bold', bg='#1b2838', fg='#ffffff').place(x=25, y=400)

tk.Label(hdd_box, text='C', font='Montserrat 12 bold', bg='#2a475e', fg='#ffffff').place(x=25, y=425)
tk.Label(hdd_box, text='H', font='Montserrat 12 bold', bg='#2a475e', fg='#ffffff').place(x=25, y=455)
tk.Label(hdd_box, text='I', font='Montserrat 12 bold', bg='#2a475e', fg='#ffffff').place(x=25, y=485)

tk.Canvas(hdd_box, width=100, height=20, bg='#c7d5e0', bd=0, highlightthickness=0).place(x=50, y=430)
tk.Canvas(hdd_box, width=100, height=20, bg='#c7d5e0', bd=0, highlightthickness=0).place(x=50, y=460)
tk.Canvas(hdd_box, width=100, height=20, bg='#c7d5e0', bd=0, highlightthickness=0).place(x=50, y=490)

if 0 < int(hdd_data[0].percent) <= 25:
    percentage_colour_c = '#90EE90'
elif 25 < int(hdd_data[0].percent) <= 50:
    percentage_colour_c = '#FEB938'
elif 50 < int(hdd_data[0].percent) <= 75:
    percentage_colour_c = '#FD9415'
elif 75 < int(hdd_data[0].percent) <= 90:
    percentage_colour_c = '#E23201'
else:
    percentage_colour_c = '#9B0002'

if 0 < int(hdd_data[1].percent) <= 25:
    percentage_colour_h = '#90EE90'
elif 25 < int(hdd_data[1].percent) <= 50:
    percentage_colour_h = '#FEB938'
elif 50 < int(hdd_data[1].percent) <= 75:
    percentage_colour_h = '#FD9415'
elif 75 < int(hdd_data[1].percent) <= 90:
    percentage_colour_h = '#E23201'
else:
    percentage_colour_h = '#9B0002'

if 0 < int(hdd_data[2].percent) <= 25:
    percentage_colour_i = '#90EE90'
elif 25 < int(hdd_data[2].percent) <= 50:
    percentage_colour_i = '#FEB938'
elif 50 < int(hdd_data[2].percent) <= 75:
    percentage_colour_i = '#FD9415'
elif 75 < int(hdd_data[2].percent) <= 90:
    percentage_colour_i = '#E23201'
else:
    percentage_colour_i = '#9B0002'

tk.Canvas(hdd_box, width=int(hdd_data[0].percent), height=20, bg=percentage_colour_c, bd=0,highlightthickness=0).place(x=50, y=430)
tk.Canvas(hdd_box, width=int(hdd_data[1].percent), height=20, bg=percentage_colour_h, bd=0,highlightthickness=0).place(x=50, y=460)
tk.Canvas(hdd_box, width=int(hdd_data[2].percent), height=20, bg=percentage_colour_i, bd=0,highlightthickness=0).place(x=50, y=490)

tk.Label(hdd_box, text=str(hdd_data[0].percent) + '%', font='Montserrat 12 bold', bg='#2a475e', fg='#ffffff').place(x=160, y=425)
tk.Label(hdd_box, text=str(hdd_data[1].percent) + '%', font='Montserrat 12 bold', bg='#2a475e', fg='#ffffff').place(x=160, y=455)
tk.Label(hdd_box, text=str(hdd_data[2].percent) + '%', font='Montserrat 12 bold', bg='#2a475e', fg='#ffffff').place(x=160, y=485)


print('\nDRAWING DASHBOARD')
# MAINLOOP
root.mainloop()