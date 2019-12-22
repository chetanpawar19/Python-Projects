"""
Project name - TheWeatherApp
Author- Chetan Pawar
"""

import requests
from tkinter import *

def display(event):
        """Display method to connect to server and display weather information to user."""
        c = Canvas(root, bg="RoyalBlue1", height=215, width=280)
        c.pack()
        city=entry_accept_cityname.get()
        try:
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=<your_secret_appid>&units=metric'.format(city)
        except Exception as msg:
                print("Unable to connect to openweathermap server. please try later!")
                print(msg)
                system.exit(0)
        res = requests.get(url)
        data = res.json()
        temperature = str(data['main']['temp'])
        wind_speed =str(data['wind']['speed'])
        latitude = str(data['coord']['lat'])
        longitude = str(data['coord']['lon'])
        description = str(data['weather'][0]['description'])
        pressure=str(data['main']['pressure'])
        humidity = str(data['main']['humidity'])
        temp_min=str(data['main']['temp_min'])
        temp_max = str(data['main']['temp_max'])
        country=str(data['sys']['country'])
        fnt = ('Helvetica', 26)
        id = c.create_text(75, 45, text=city+','+country, font=fnt,fill='white')
        fnt = ('Helvetica', 10)
        id = c.create_text(210, 35, text='Latitude- '+latitude, font=fnt, fill='white')
        fnt = ('Helvetica', 10)
        id = c.create_text(210, 53, text='  Longitude- ' + longitude, font=fnt, fill='white')
        fnt = ('Helvetica', 30)
        id = c.create_text(193, 104, text=temperature, font=fnt, fill='white')
        fnt = ('Helvetica', 13)
        id = c.create_text(256, 85, text='oC', font=fnt, fill='white')
        fnt = ('Helvetica', 10)
        id = c.create_text(70, 95, text='Temp. Max- '+temp_max, font=fnt, fill='white')
        fnt = ('Helvetica', 10)
        id = c.create_text(70, 114, text='Temp. Min- '+temp_min, font=fnt, fill='white')
        fnt = ('Helvetica', 28)
        id = c.create_text(83, 155, text=description, font=fnt, fill='white')
        fnt = ('Helvetica', 10)
        id = c.create_text(203, 150, text='Humidity- ' + humidity, font=fnt, fill='white')
        fnt = ('Helvetica', 10)
        id = c.create_text(219, 169, text='Pressure- ' + pressure, font=fnt, fill='white')
        fnt = ('Helvetica', 8)
        id = c.create_text(138, 199, text='Designed by Chetan Pawar', font=fnt, fill='white')


root=Tk()
root.title('The Weather App')
c=Canvas(root,bg="RoyalBlue1",height=92,width=280)
c.pack()
fnt=('Helvetica',12)
id=c.create_text(140,20,text='Search weather, type city name',font=fnt,fill='white')
entry_accept_cityname=Entry(c,width=35,bg='white')
entry_accept_cityname.bind('<Return>',display)
entry_accept_cityname.place(x=32,y=40)
fnt=('Helvetica',8)
id=c.create_text(140,75,text='Powered by OpenWeatherMap.org',font=fnt,fill='white')
root.mainloop()
